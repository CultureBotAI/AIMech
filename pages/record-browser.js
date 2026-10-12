/* Client-side search and filtering for AIMech concepts */
(function () {
  'use strict';

  function initBrowser() {
    var searchInput = document.getElementById('searchInput');
    var originSelect = document.getElementById('originSelect');
    var kindSelect = document.getElementById('kindSelect');
    var branchSelect = document.getElementById('branchSelect');
    var resetBtn = document.getElementById('resetFilters');
    var countEl = document.getElementById('matchCount');
    var totalEl = document.getElementById('totalCount');
    var table = document.getElementById('conceptTable');

    if (!table) return;

    var rows = Array.from(table.querySelectorAll('tbody tr'));
    var totalRows = rows.length;

    function applyFilters() {
      var query = (searchInput ? searchInput.value : '').trim().toLowerCase();
      var origin = (originSelect ? originSelect.value : 'all');
      var kind = (kindSelect ? kindSelect.value : 'all');
      var branch = (branchSelect ? branchSelect.value : 'all');

      var visibleCount = 0;

      rows.forEach(function (row) {
        var rowOrigin = row.getAttribute('data-origin') || '';
        var rowKind = row.getAttribute('data-kind') || '';
        var rowBranches = (row.getAttribute('data-branch') || '').split(' ');
        var rowSearch = (row.getAttribute('data-search') || '').toLowerCase();

        var matchOrigin = (origin === 'all' || rowOrigin === origin);
        var matchKind = (kind === 'all' || rowKind === kind);
        var matchBranch = (branch === 'all' || rowBranches.indexOf(branch) !== -1);
        var matchQuery = true;

        if (query) {
          var terms = query.split(/\s+/);
          matchQuery = terms.every(function (term) {
            return rowSearch.indexOf(term) !== -1;
          });
        }

        if (matchOrigin && matchKind && matchBranch && matchQuery) {
          row.style.display = '';
          visibleCount++;
        } else {
          row.style.display = 'none';
        }
      });

      if (countEl) countEl.textContent = visibleCount;
      if (totalEl) totalEl.textContent = totalRows;

      // Update URL search parameters without reloading
      var params = new URLSearchParams();
      if (query) params.set('q', query);
      if (origin !== 'all') params.set('origin', origin);
      if (kind !== 'all') params.set('kind', kind);
      if (branch !== 'all') params.set('branch', branch);

      var newUrl = window.location.pathname + (params.toString() ? '?' + params.toString() : '');
      window.history.replaceState({}, '', newUrl);
    }

    // Populate from URL params on initial load
    var urlParams = new URLSearchParams(window.location.search);
    if (urlParams.has('q') && searchInput) searchInput.value = urlParams.get('q');
    if (urlParams.has('origin') && originSelect) originSelect.value = urlParams.get('origin');
    if (urlParams.has('kind') && kindSelect) kindSelect.value = urlParams.get('kind');
    if (urlParams.has('branch') && branchSelect) branchSelect.value = urlParams.get('branch');

    // Event listeners
    if (searchInput) searchInput.addEventListener('input', applyFilters);
    if (originSelect) originSelect.addEventListener('change', applyFilters);
    if (kindSelect) kindSelect.addEventListener('change', applyFilters);
    if (branchSelect) branchSelect.addEventListener('change', applyFilters);

    if (resetBtn) {
      resetBtn.addEventListener('click', function () {
        if (searchInput) searchInput.value = '';
        if (originSelect) originSelect.value = 'all';
        if (kindSelect) kindSelect.value = 'all';
        if (branchSelect) branchSelect.value = 'all';
        applyFilters();
      });
    }

    applyFilters();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initBrowser);
  } else {
    initBrowser();
  }
})();
