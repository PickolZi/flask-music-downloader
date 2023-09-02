const selectedPlaylists = document.querySelectorAll('.playlist');

// Assigns event listener that when any playlist is clicked, the user
// is redirected to the webpage.
selectedPlaylists.forEach((playlist) => {
    playlist.addEventListener("click", () => {
        let href = playlist.getElementsByTagName('a')[0];
        href = href.getAttribute('href');
        location.replace(href);
    });
});