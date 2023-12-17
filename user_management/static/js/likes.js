document.addEventListener('DOMContentLoaded', function() {
    var likePostUrl = document.body.getAttribute('data-like-post-url');
    var csrfToken = document.body.getAttribute('data-csrf-token');
});

function likePost(postId) {
    fetch(likePostUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': csrfToken
        },
        body: 'id=' + postId
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('like-count-' + postId).textContent = data.likes_count;
        const likeButton = document.getElementById('like-button-' + postId);
        likeButton.textContent = data.is_liked ? 'Odlub' : 'Lubię to!';
    })
    .catch(error => console.error('Error:', error));
}
