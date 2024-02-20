// Example JavaScript code for your Flask application

// This function can be used to perform some action when the document is fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Example: Alert a message when the button is clicked
    var addButton = document.getElementById('add-button');
    if (addButton) {
        addButton.addEventListener('click', function() {
            alert('Button clicked!');
        });
    }
});
