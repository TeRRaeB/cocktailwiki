document.addEventListener("DOMContentLoaded", function() {
    const loadMoreButton = document.getElementById("load-more");
    if (loadMoreButton) {
        loadMoreButton.addEventListener("click", function() {
            const page = loadMoreButton.getAttribute("data-page") || 2;

            fetch(`/load-more-posts/?page=${page}`)
                .then(response => response.json())
                .then(data => {
                    document.getElementById("posts-container").insertAdjacentHTML("beforeend", data.posts_html);
                    loadMoreButton.setAttribute("data-page", parseInt(page) + 1);

                    if (!data.has_next) {
                        loadMoreButton.style.display = "none";
                    }
                })
                .catch(error => console.error("Error loading more posts:", error));
        });
    }
});
