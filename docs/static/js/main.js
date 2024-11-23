document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('searchInput');
    const searchResults = document.getElementById('searchResults');
    const genderFilter = document.getElementById('genderFilter');
    const rashiFilter = document.getElementById('rashiFilter');
    const sortBy = document.getElementById('sortBy');
    const featuredNames = document.getElementById('featuredNames');
    let debounceTimer;

    // Function to perform search
    function performSearch() {
        const query = searchInput.value.trim();
        const gender = genderFilter.value;
        const rashi = rashiFilter.value;
        const sort = sortBy.value;
        
        if (query.length < 2 && !gender && !rashi && !sort) {
            searchResults.style.display = 'none';
            return;
        }

        const params = new URLSearchParams({
            q: query,
            gender: gender,
            rashi: rashi,
            sort: sort
        });

        fetch(`/api/search?${params.toString()}`)
            .then(response => response.json())
            .then(data => {
                if (data.length > 0) {
                    searchResults.innerHTML = data.map(item => `
                        <div class="search-result-item" onclick="window.location.href='${item.url}'">
                            <div class="row align-items-center">
                                <div class="col-md-8">
                                    <strong>${item.name}</strong> 
                                    ${item.sanskrit_script ? `<small class="text-muted">(${item.sanskrit_script})</small>` : ''}
                                    <br>
                                    <small class="text-muted">${item.meaning}</small>
                                </div>
                                <div class="col-md-4 text-end">
                                    <span class="badge bg-primary">${item.gender}</span>
                                    ${item.popularity ? `<span class="badge bg-success">${item.popularity}</span>` : ''}
                                </div>
                            </div>
                        </div>
                    `).join('');
                    searchResults.style.display = 'block';
                } else {
                    searchResults.innerHTML = '<div class="search-result-item">No results found</div>';
                    searchResults.style.display = 'block';
                }
            });
    }

    // Load featured names
    function loadFeaturedNames() {
        fetch('/api/search?sort=popularity')
            .then(response => response.json())
            .then(data => {
                const popularNames = data.slice(0, 6);
                featuredNames.innerHTML = popularNames.map(item => `
                    <div class="col-md-4 mb-4">
                        <div class="name-card h-100">
                            <h3>${item.name}</h3>
                            ${item.sanskrit_script ? `<div class="sanskrit-script">${item.sanskrit_script}</div>` : ''}
                            <p class="text-muted">${item.meaning}</p>
                            <div class="mb-2">
                                <span class="badge bg-primary">${item.gender}</span>
                                ${item.popularity ? `<span class="badge bg-success">${item.popularity}</span>` : ''}
                            </div>
                            <a href="${item.url}" class="btn btn-outline-primary btn-sm">View Details</a>
                        </div>
                    </div>
                `).join('');
            });
    }

    // Event listeners
    searchInput.addEventListener('input', function() {
        clearTimeout(debounceTimer);
        debounceTimer = setTimeout(performSearch, 300);
    });

    genderFilter.addEventListener('change', performSearch);
    rashiFilter.addEventListener('change', performSearch);
    sortBy.addEventListener('change', performSearch);

    // Close search results when clicking outside
    document.addEventListener('click', function(e) {
        if (!searchResults.contains(e.target) && e.target !== searchInput) {
            searchResults.style.display = 'none';
        }
    });

    // Load featured names on page load
    loadFeaturedNames();
});
