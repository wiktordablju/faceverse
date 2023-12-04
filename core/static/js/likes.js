function likePost(postId) {
    fetch(likePostUrl, { // Use the variable from the HTML template
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': csrfToken // Use the variable from the HTML template
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
