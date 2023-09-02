const toggleAllCheckbox = document.querySelector('.toggle-all');
const otherCheckboxes = document.querySelectorAll('.other-checkbox');
const songs = document.querySelectorAll('.song');

otherCheckboxes.forEach((checkbox) => {
    // Fixes bug when checkbox is clicked, it does not change states.
    checkbox.addEventListener('click', () => {
        const checkboxState = checkbox.checked;

        if (checkboxState) {
            checkbox.checked = false;
        } else {
            checkbox.checked = true;
        }

    });
});

songs.forEach((song) => {
    // When any part of the "song" class is clicked, check or uncheck the checkbox for the corresponding song.
    song.addEventListener('click', () => {
        let checkbox = song.querySelector('input')
        const isChecked = checkbox.checked;

        if (isChecked) {
            checkbox.checked = false;

            // if the toggle-all checkbox is checked, uncheck it. 
            if (toggleAllCheckbox.checked) {
                toggleAllCheckbox.checked = false;
            }
        } else {
            checkbox.checked = true;
        }
    });
});

toggleAllCheckbox.addEventListener('click', () => {
    // When the toggle-all checkbox is toggled on or off, check or uncheck all other check boxes
    let checkbox = toggleAllCheckbox;
    const isChecked = checkbox.checked;

    if (isChecked) {
        songs.forEach((song) => {
            song.querySelector('input').checked = true;
        });
    } else {
        songs.forEach((song) => {
            song.querySelector('input').checked = false;
        });
    }
});
