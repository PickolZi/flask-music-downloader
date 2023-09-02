const playlistsIcon = document.querySelector(".playlists__icon");
const playlists = document.querySelector(".playlists");

playlistsIcon.addEventListener("click", () => {
    let playlistsDisplay = getComputedStyle(playlists).display;

    if (playlistsDisplay == "none") {
        playlists.style.display = "inline";

        // Moves icon playlists icon out of way to the right.
        playlistsIcon.classList.remove("playlists__icon-left");
        playlistsIcon.classList.add("playlists__icon-right");
    } else {
        playlists.style.display = "none";

        // Moves icon playlists icon back to the left.
        playlistsIcon.classList.remove("playlists__icon-right");
        playlistsIcon.classList.add("playlists__icon-left");
    }
});