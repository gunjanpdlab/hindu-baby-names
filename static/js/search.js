// Live Search Function
function performSearch() {
    const searchInput = document.getElementById('searchInput');
    const genderFilter = document.getElementById('genderFilter');
    const rashiFilter = document.getElementById('rashiFilter');
    const sortBy = document.getElementById('sortBy');
    const resultsContainer = document.getElementById('searchResults');

    // Only search if there's input
    if (!searchInput.value.trim()) {
        resultsContainer.innerHTML = '';
        return;
    }

    // Build query parameters
    const params = new URLSearchParams({
        q: searchInput.value.trim(),
        gender: genderFilter.value,
        rashi: rashiFilter.value,
        sort: sortBy.value
    });

    // Make API call
    fetch(`/api/search?${params.toString()}`)
        .then(response => response.json())
        .then(results => {
            if (results.length === 0) {
                resultsContainer.innerHTML = `
                    <div class="no-results">
                        <p>No names found matching your search criteria.</p>
                        <p>Try:</p>
                        <ul>
                            <li>Using different keywords</li>
                            <li>Checking the spelling</li>
                            <li>Removing filters</li>
                            <li>Browsing names by alphabet instead</li>
                        </ul>
                    </div>`;
                return;
            }

            // Build results HTML
            const resultsHTML = results.map(name => `
                <div class="name-card ${name.popularity.is_popular ? 'popular' : ''}">
                    <h3>
                        <a href="${name.url}">${name.name}</a>
                        ${name.popularity.is_popular ? '<span class="popular-badge">Popular</span>' : ''}
                    </h3>
                    <div class="name-info">
                        <span class="gender-tag ${name.gender.toLowerCase()}">${name.gender}</span>
                        <p class="meaning">${name.meaning}</p>
                    </div>
                    <div class="card-footer">
                        <a href="${name.url}" class="view-details">View Details</a>
                    </div>
                </div>
            `).join('');

            resultsContainer.innerHTML = `<div class="results-grid">${resultsHTML}</div>`;
        })
        .catch(error => {
            console.error('Search error:', error);
            resultsContainer.innerHTML = `
                <div class="error-message">
                    <p>Sorry, something went wrong with the search. Please try again.</p>
                </div>`;
        });
}

// Add event listeners
document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('searchInput');
    const genderFilter = document.getElementById('genderFilter');
    const rashiFilter = document.getElementById('rashiFilter');
    const sortBy = document.getElementById('sortBy');

    // Debounce function
    function debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    }

    // Add event listeners with debounced search
    const debouncedSearch = debounce(performSearch, 300);
    searchInput.addEventListener('input', debouncedSearch);
    genderFilter.addEventListener('change', performSearch);
    rashiFilter.addEventListener('change', performSearch);
    sortBy.addEventListener('change', performSearch);
});
