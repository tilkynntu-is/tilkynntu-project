// Tryggvi Snær Barðarson 2024 7/10
console.log("JavaScript file is successfully connected!");

const leafletMap = L;
let postMap;

// fall til að fá post data
fetch('/static/json/posts.json?' + new Date().getTime()) // Add query param to prevent caching
    .then(response => response.json())
    .then(data => {
        console.log("JSON file successfully connected.");
        displayPost(data[0]); // Birta fyrsta post by default
    });

// fall til að birta post data
function displayPost(post) {
    // Seta mynd
    const postImage = document.getElementById("post-image");
    postImage.src = post.image || "placholder";
    postImage.alt = post.title || "No Image Available";

    // Seta titil
    const postTitle = document.getElementById("post-title");
    postTitle.textContent = post.title || "Untitled";


    const postInfo = document.getElementById("post-information");
    postInfo.textContent = post.information || "No additional information.";

 
    const postCity = document.getElementById("post-city");
    postCity.textContent = `City: ${post.location.city || "Unknown"}`;

    // will fix this part later
    const postDate = document.getElementById("post-date");
    dayjs.locale('is');
    const formattedDate = post.postDate ? dayjs(post.postDate).format("D MMMM YYYY") : "Unknown Date";
    postDate.textContent = `Posted on: ${formattedDate}`;

    // Seta tags
    const tagsContainer = document.getElementById("post-tags");
    tagsContainer.innerHTML = ''; // Clear existing tags

    if (post.tags && Object.keys(post.tags).length > 0) {
        Object.keys(post.tags).forEach(key => {
            const tagElement = document.createElement('span');
            tagElement.textContent = `${key}: ${post.tags[key]}`;
            tagElement.className = "bg-blue-100 text-blue-800 text-xs font-medium px-2.5 py-0.5 rounded dark:bg-gray-700 dark:text-blue-400 border border-blue-400";
            tagsContainer.appendChild(tagElement);
        });
    } else {
        tagsContainer.textContent = "No tags available.";
    }

    // Seta staðsetningu á kort
    showMap(post.location.lat, post.location.lng);
}

// sýna með leaflet
function showMap(lat, lng) {
    const mapElement = document.getElementById("map");

    if (postMap) {
        postMap.remove(); // Fjarlægja gamalt kort
    }

    postMap = leafletMap.map(mapElement).setView([lat, lng], 13); // Seta view á cordinata

    // Bæta við OpenStreetMap tile layer
    leafletMap.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
    }).addTo(postMap);

    leafletMap.marker([lat, lng]).addTo(postMap)
        .bindPopup(`Location: ${lat}, ${lng}`)
        .openPopup();
}
