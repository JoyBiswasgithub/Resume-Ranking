// Example JavaScript for additional interactivity
document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');
    if (form) {
        form.addEventListener('submit', () => {
            // Add a loading animation or message here if desired
            form.querySelector('button').innerText = 'Submitting...';
        });
    }
});
