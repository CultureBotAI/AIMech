/* Client-side search, filtering, and sorting for AIMech concepts */
(function () {
  'use strict';

  function initBrowser() {
    var searchInput = document.getElementById('searchInput');
    var sortSelect = document.getElementById('sortSelect');
    var originSelect = document.getElementById('originSelect');
    var kindSelect = document.getElementById('kindSelect');
    var branchSelect = document.getElementById('branchSelect');
    var resetBtn = document.getElementById('resetFilters');
    var countEl = document.getElementById('matchCount');
    var totalEl = document.getElementById('totalCount');
    var emptyEl = document.getElementById('emptyState');
    var table = document.getElementById('conceptTable');

    if (!table) return;

    var tbody = table.querySelector('tbody');
    var rows = Array.from(tbody.querySelectorAll('tr'));
    var totalRows = rows.length;

    function sortRows(mode) {
      if (!tbody) return;
      var sorted = rows.slice().sort(function (a, b) {
        var nameA = a.getAttribute('data-name') || '';
        var nameB = b.getAttribute('data-name') || '';
        if (mode === 'name-desc') {
          return nameB.localeCompare(nameA);
        }
        if (mode === 'claims-desc') {
          var clDiff = (parseInt(b.getAttribute('data-claims') || '0', 10) || 0) -
                       (parseInt(a.getAttribute('data-claims') || '0', 10) || 0);
          return clDiff !== 0 ? clDiff : nameA.localeCompare(nameB);
        }
        if (mode === 'sources-desc') {
          var srcDiff = (parseInt(b.getAttribute('data-sources') || '0', 10) || 0) -
                        (parseInt(a.getAttribute('data-sources') || '0', 10) || 0);
          return srcDiff !== 0 ? srcDiff : nameA.localeCompare(nameB);
        }
        if (mode === 'origin-asc') {
          var origA = a.getAttribute('data-origin') === 'curated' ? 0 : 1;
          var origB = b.getAttribute('data-origin') === 'curated' ? 0 : 1;
          return origA !== origB ? origA - origB : nameA.localeCompare(nameB);
        }
        if (mode === 'id-asc') {
          var idA = a.getAttribute('data-id') || '';
          var idB = b.getAttribute('data-id') || '';
          return idA.localeCompare(idB);
        }
        return nameA.localeCompare(nameB);
      });
      sorted.forEach(function (row) {
        tbody.appendChild(row);
      });
      rows = sorted;
    }

    function applyFilters() {
      var typed = (searchInput ? searchInput.value : '').trim();
      var query = typed.toLowerCase();
      var sortMode = (sortSelect ? sortSelect.value : 'name-asc');
      var origin = (originSelect ? originSelect.value : 'all');
      var kind = (kindSelect ? kindSelect.value : 'all');
      var branch = (branchSelect ? branchSelect.value : 'all');

      sortRows(sortMode);

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
      if (emptyEl) emptyEl.hidden = visibleCount !== 0;

      // Update URL search parameters without reloading; the query keeps its case
      var params = new URLSearchParams();
      if (typed) params.set('q', typed);
      if (sortMode && sortMode !== 'name-asc') params.set('sort', sortMode);
      if (origin !== 'all') params.set('origin', origin);
      if (kind !== 'all') params.set('kind', kind);
      if (branch !== 'all') params.set('branch', branch);

      var newUrl = window.location.pathname + (params.toString() ? '?' + params.toString() : '');
      window.history.replaceState({}, '', newUrl);
    }

    // A shared URL can carry a value this listing does not offer (a mistyped
    // origin, a kind that was renamed). Keep the control's default rather than
    // selecting nothing, which hid every row or ignored the filter silently.
    function restoreSelect(select, value) {
      if (!select || value === null) return;
      for (var i = 0; i < select.options.length; i++) {
        if (select.options[i].value === value) {
          select.value = value;
          return;
        }
      }
    }

    // Populate from URL params on initial load
    var urlParams = new URLSearchParams(window.location.search);
    if (urlParams.has('q') && searchInput) searchInput.value = urlParams.get('q');
    restoreSelect(sortSelect, urlParams.get('sort'));
    restoreSelect(originSelect, urlParams.get('origin'));
    restoreSelect(kindSelect, urlParams.get('kind'));
    restoreSelect(branchSelect, urlParams.get('branch'));

    // Event listeners
    if (searchInput) searchInput.addEventListener('input', applyFilters);
    if (sortSelect) sortSelect.addEventListener('change', applyFilters);
    if (originSelect) originSelect.addEventListener('change', applyFilters);
    if (kindSelect) kindSelect.addEventListener('change', applyFilters);
    if (branchSelect) branchSelect.addEventListener('change', applyFilters);

    if (resetBtn) {
      resetBtn.addEventListener('click', function () {
        if (searchInput) searchInput.value = '';
        if (sortSelect) sortSelect.value = 'name-asc';
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
