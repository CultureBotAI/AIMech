"""Curator moment/conditioning examples, not fitted GP or benchmark replication."""
import json
import math


def calculate():
    # Linear Gaussian observation of a two-dimensional state.
    prior_mean = [1., -1.]
    prior_covariance = [[2., 0.], [0., 3.]]
    observation_matrix = [1., 2.]
    noise_variance = .5
    observation = 2.
    predicted_observation_mean = sum(a*b for a, b in zip(observation_matrix, prior_mean))
    cross = [sum(prior_covariance[i][j]*observation_matrix[j] for j in range(2)) for i in range(2)]
    predicted_observation_variance = sum(a*b for a, b in zip(observation_matrix, cross)) + noise_variance
    posterior_mean = [prior_mean[i]+cross[i]*(observation-predicted_observation_mean)/predicted_observation_variance for i in range(2)]
    posterior_covariance = [[prior_covariance[i][j]-cross[i]*cross[j]/predicted_observation_variance for j in range(2)] for i in range(2)]
    determinant = posterior_covariance[0][0]*posterior_covariance[1][1]-posterior_covariance[0][1]*posterior_covariance[1][0]
    assert math.isclose(determinant, 6*noise_variance/predicted_observation_variance)
    assert determinant > 0 and posterior_covariance[0][0] > 0
    assert math.isclose(posterior_covariance[0][1], posterior_covariance[1][0])
    # X standard Gaussian, Y=X^2: joint moments exact but nonlinear conditioning.
    nonlinear = [dict(observation=y,exact_conditional_mean=0.,exact_conditional_variance=y,
                      gaussian_projected_mean=0.,gaussian_projected_variance=1.) for y in [.25, 1., 4.]]
    assert nonlinear[0]['exact_conditional_variance'] != nonlinear[0]['gaussian_projected_variance']
    assert nonlinear[2]['exact_conditional_variance'] != nonlinear[2]['gaussian_projected_variance']
    # Independent conditional residuals do not imply marginally independent outputs.
    # Y1=X+eps1, Y2=2X+eps2; VarX=1, independent residual variances .3,.7.
    shared_input_covariance = [[1.3, 2.], [2., 4.7]]
    assert shared_input_covariance[0][1] == 2.
    assert shared_input_covariance[0][0]*shared_input_covariance[1][1]-4 > 0
    return dict(
        scope='Finite analytic moment and conditioning illustrations; no GP fitting, trajectory simulation or source benchmark execution.',
        linear_gaussian=dict(prior_mean=prior_mean,prior_covariance=prior_covariance,H=observation_matrix,
                             observation=observation,measurement_noise_variance=noise_variance,
                             input_output_covariance=cross,predicted_observation_variance=predicted_observation_variance,
                             posterior_mean=posterior_mean,posterior_covariance=posterior_covariance,determinant=determinant),
        nonlinear_conditioning=dict(model='X~N(0,1), Y=X^2; E[Y]=1, Var[Y]=2, Cov[X,Y]=0.',
                                    conditional_law='For y>0, X given Y=y has equal mass at plus/minus sqrt(y).',
                                    examples=nonlinear),
        shared_input=dict(model='Y1=X+eps1,Y2=2X+eps2; VarX=1 and independent residual variances .3,.7.',
                          conditional_cross_covariance=0.,marginal_covariance=shared_input_covariance),
        interpretation=['Correct joint-Gaussian conditioning uses the transposed cross-covariance and includes independent observation noise once.',
                        'Exact joint first two moments do not give exact nonlinear posterior moments after Gaussian joint projection.',
                        'Conditionally independent output models can have correlated outputs after integrating a shared uncertain input.'])


if __name__ == '__main__':
    print(json.dumps(calculate(), indent=2))
