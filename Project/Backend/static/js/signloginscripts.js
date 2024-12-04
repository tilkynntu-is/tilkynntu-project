// Test to ensure JavaScript is connected
console.log("JavaScript file is successfully connected!");

// veit að það er mjög mikið af spelling errors var að flíta mér smá 


// Global variable to hold user data
let users = [];

// get user data from the JSON file 
fetch('/static/json/signins.json')
    .then(response => {
        if (!response.ok) {
            throw new Error(`Náði ekki að loda json file: ${response.statusText}`);
        }
        console.log("json file náði að tengjast.");
        return response.json();
    })
    .then(data => {
        console.log('User data:', data);
        users = data; // Save users for login and signup validation
        initializeForms();
    })
    .catch(error => {
        console.error('Error loda user data:', error);
        showNotification("Error loda. please reindu aftur anan tíma.", "error");
    });

// Function to initialize login and sign-up forms
function initializeForms() {
    console.log("Forms initialized með user data:", users);

    document.getElementById("login-form").addEventListener("submit", handleLogin);
    document.getElementById("signup-form").addEventListener("submit", handleSignup);
    document.getElementById("toggle-form").addEventListener("click", toggleForms);
}

// Function to handle login
function handleLogin(event) {
    event.preventDefault();

    const firstname = document.getElementById("login-username").value.trim();
    const password = document.getElementById("login-password").value.trim();

    if (password.length < 6) {
        showNotification("Password must be at least 6 characters long.", "error");
        console.log("Login failed: Password is less than 6 characters.");
        return;
    }

    const user = users.find(u => u.firstname.toLowerCase() === firstname.toLowerCase());

    if (user) {
        if (user.password === password) {
            showNotification(`Welcome, ${user.firstname}! Login successful.`, "success");
            displaySuccessMessage(`Welcome, ${user.firstname}!`);
            console.log("Login successful: Rét username og Leiniorð.");
        } else {
            showNotification("Incorrect password. reindi aftur á eftir.", "error");
            console.log("Login failed: villaust password.");
        }
    } else {
        showNotification("User fundin ekki. signdu up first.", "error");
        console.log("Login failed: user ekki fundin.");
    }
}

// Function to handle sign-up
function handleSignup(event) {
    event.preventDefault();

    const firstname = document.getElementById("signup-firstname").value.trim();
    const lastname = document.getElementById("signup-lastname").value.trim();
    const birthday = document.getElementById("signup-birthday").value.trim();
    const password = document.getElementById("signup-password").value.trim();

    if (!firstname || !lastname || !birthday || !password) {
        showNotification("þú þarft í öll fields fyrir sign up.", "error");
        console.log("Sign-up failed: ert að misa fields.");
        return;
    }

    if (password.length < 6) {
        showNotification("Password þarf að vera at least 6 characters lángt.", "error");
        console.log("Sign-up failaði password þarf að vera 6 characters eða lengra.");
        return;
    }

    const newUser = { firstname, lastname, birthday, password };
    users.push(newUser);

    showNotification("Sign-up successful! þú getur nuna loga in.", "success");
    console.log("Sign-up successful: user bæt við list.", newUser);
    document.getElementById("signup-form").reset();
    toggleForms();
}

// Function to toggle between login and sign-up forms
function toggleForms() {
    const loginForm = document.getElementById("login-form");
    const signupForm = document.getElementById("signup-form");

    loginForm.classList.toggle("hidden");
    signupForm.classList.toggle("hidden");

    const toggleText = loginForm.classList.contains("hidden")
        ? "Áttu nú þegar aðgang? Skráðu inn hér"
        : "Ekki með aðgang? Gerðu eitt hér";
    document.getElementById("toggle-form").textContent = toggleText;
}


function showNotification(message, type = "info") {
    const notification = document.createElement("div");
    notification.textContent = message;
    notification.className = `notification-${type} p-4 mb-4 rounded bg-${type === "error" ? "red" : "blue"}-500 text-white shadow-md`;
    document.body.appendChild(notification);

    setTimeout(() => notification.remove(), 3000);
}


function displaySuccessMessage(message) {
    const messageContainer = document.getElementById("success-message");

    if (!messageContainer) {
        const newMessageContainer = document.createElement("div");
        newMessageContainer.id = "success-message";
        newMessageContainer.className = "p-4 mt-4 rounded bg-green-500 text-white text-center shadow-lg";
        newMessageContainer.textContent = message;

        const formContainer = document.getElementById("form-container");
        formContainer.parentNode.insertBefore(newMessageContainer, formContainer);

        setTimeout(() => {
            newMessageContainer.remove();
        }, 5000);
    }
}
