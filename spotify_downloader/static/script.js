// Event Listeners for the checkboxes
document.addEventListener('DOMContentLoaded', function() {
    const toggleAllCheckbox = document.querySelector('.toggle-all');
    const otherCheckboxes = document.querySelectorAll('.other-checkbox');

    toggleAllCheckbox.addEventListener('change', function() {
        const isChecked = toggleAllCheckbox.checked;

        otherCheckboxes.forEach(function(checkbox) {
            checkbox.checked = isChecked;
        });
    });

    otherCheckboxes.forEach(function(checkbox) {
        checkbox.addEventListener('change', function() {
            if (!this.checked) {
                toggleAllCheckbox.checked = false;
            }
        });
    });
});


document.addEventListener('DOMContentLoaded', function() {
    const songLabel = document.querySelectorAll('.song');

    songLabel.forEach(function(song) {
        song.addEventListener('click', function() {
            if (this.querySelector(".other-checkbox").checked) {
                this.querySelector(".other-checkbox").checked = false;
            } else {
                this.querySelector(".other-checkbox").checked = true;
            }
        });
    });
});