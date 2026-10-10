"""Closed LinkML validation and local provenance checks."""

import json
from datetime import datetime
from functools import lru_cache
from importlib.resources import as_file, files
from pathlib import Path

import yaml
from jsonschema import FormatChecker
from jsonschema.validators import validator_for
from linkml.generators.jsonschemagen import JsonSchemaGenerator


class UniqueKeyLoader(yaml.SafeLoader):
    def construct_mapping(self, node, deep=False):
        self.flatten_mapping(node)
        result = {}
        for key_node, value_node in node.value:
            key = self.construct_object(key_node, deep=deep)
            if not isinstance(key, str) or key in result:
                raise yaml.constructor.ConstructorError(
                    None, None, "duplicate or non-string mapping key", key_node.start_mark
                )
            result[key] = self.construct_object(value_node, deep=deep)
        return result


def read_record(path: Path):
    return yaml.load(path.read_text(encoding="utf-8"), Loader=UniqueKeyLoader)


@lru_cache(maxsize=4)
def schema_validator(filename="aimech.yaml", top_class="AIConcept"):
    with as_file(files("aimech").joinpath("schema", filename)) as path:
        schema = json.loads(JsonSchemaGenerator(
            str(path), top_class=top_class, not_closed=False, include_null=False
        ).serialize())
    validator = validator_for(schema)
    validator.check_schema(schema)
    return validator(schema, format_checker=FormatChecker())


def record_validator():
    return schema_validator()


def validate_record(record):
    errors = [
        f"{'/'.join(map(str, e.absolute_path)) or '$'}: {e.message}"
        for e in record_validator().iter_errors(record)
    ]
    if errors:
        return sorted(errors)
    iri = "https://w3id.org/aio/" + record["id"].split(":", 1)[1]
    if record["ontology_iri"] != iri or record["provenance"]["source_node"] != iri:
        errors.append("id, ontology_iri and provenance/source_node must identify the same AIO class")
    for field in ("name", "definition"):
        if not record[field].strip():
            errors.append(f"{field}: must be nonempty")
    for field in ("branches", "parents", "subsets", "definition_sources", "history_refs"):
        values = record.get(field, [])
        if len(values) != len(set(values)):
            errors.append(f"{field}: duplicate values")
    stamps = [record["provenance"]["imported_at"]]
    stamps.extend(e["timestamp"] for e in record.get("curation_history", []))
    for stamp in stamps:
        try:
            parsed = datetime.fromisoformat(stamp.replace("Z", "+00:00"))
            if parsed.tzinfo is None:
                raise ValueError("timezone required")
        except ValueError:
            errors.append(f"invalid timezone-aware timestamp: {stamp}")
    if record["provenance"]["license"] != "CC-BY-4.0":
        errors.append("AIO-derived records must retain CC-BY-4.0 attribution")
    return sorted(errors)
