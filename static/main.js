document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("chatForm");
    const responseContainer = document.getElementById("response");

    form.addEventListener("submit", function(e) {
        e.preventDefault(); // Prevent the default form submission behavior

        const formData = new FormData(form);
        const data = Object.fromEntries(formData.entries());

        fetch('/chatbot', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        })
        .then(response => response.json())
        .then(data => {
            // Display the response from Flask/OpenAI in the 'response' div
            responseContainer.textContent = data.message;
        })
        .catch(error => {
            console.error('Error:', error);
            responseContainer.textContent = 'Failed to get response.';
        });
    });
});
