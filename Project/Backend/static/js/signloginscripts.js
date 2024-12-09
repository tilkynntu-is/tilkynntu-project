document.addEventListener("DOMContentLoaded", () => {
    console.log("JavaScript loaded and DOM fully initialized!");

    // CSRF token retrieval
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]')?.value;

    // Initialize forms
    const loginForm = document.getElementById("login-form");
    const signupForm = document.getElementById("signup-form");
    const toggleLink = document.getElementById("toggle-form");
    const authForm = document.getElementById("auth-form");
    const usernameDisplay = document.getElementById("username-display");

    // Handle login form submission
    if (loginForm) {
        loginForm.addEventListener("submit", async (event) => {
            event.preventDefault(); // Prevent default form submission

            const username = document.getElementById("login-username").value;
            const password = document.getElementById("login-password").value;

            try {
                const response = await fetch('/auth/login/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': csrftoken, // Include CSRF token
                    },
                    body: JSON.stringify({ username, password }),
                });

            } catch (error) {
                console.error("Error during login:", error);
                alert("An unexpected error occurred. Please try again.");
            }
        });
    } else {
        console.warn("Login form not found on the page.");
    }

    // Handle signup form submission
    if (signupForm) {
        signupForm.addEventListener("submit", async (event) => {
            event.preventDefault();

            const firstName = document.getElementById("signup-firstname").value;
            const username = document.getElementById("signup-username").value;
            const email = document.getElementById("signup-email").value;
            const password = document.getElementById("signup-password").value;

            try {
                const response = await fetch('/auth/signup/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': csrftoken, // Include CSRF token 
                        // reminder that a CSRF 
                        // This token is included in forms or requests sent by the user 
                        // and is checked by the server to verify that the request 
                        // is coming from the authenticated user and not from a malicious source.
                    },
                    body: JSON.stringify({ first_name: firstName, username, email, password }),
                });

                const result = await response.json();
                if (response.ok) {
                    alert("Account created successfully! Redirecting to login page.");
                    window.location.href = '/auth/login/'; // Redirect to login page
                } else {
                    alert("Sign-up failed: " + (result.error || "Invalid data"));
                }
            } catch (error) {
                console.error("Error during sign-up:", error);
                alert("An unexpected error occurred. Please try again.");
            }
        });
    } else {
        console.warn("Signup form not found on the page.");
    }

    // Toggle between login and signup forms didnt wanna have seperate html files but maybe that was a bad idea
    if (toggleLink) {
        toggleLink.addEventListener("click", () => {
            if (loginForm && signupForm) {
                loginForm.classList.toggle("hidden");
                signupForm.classList.toggle("hidden");
                toggleLink.textContent =
                    loginForm.classList.contains("hidden")
                        ? "Fyrir innskráningu? Skráðu þig hér"
                        : "Ekki með aðgang? Gerðu eitt hér";
            }
        });
    }

 
    if (authForm) {
        authForm.addEventListener("submit", (e) => {
            e.preventDefault();

            const usernameInput = document.querySelector("input[name='username']");

          
            authForm.submit();
        });
    }
});
