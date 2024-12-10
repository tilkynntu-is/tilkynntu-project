// JavaScript file is successfully connected!
console.log("JavaScript file is successfully connected!");

// On page load or when changing themes, best to add inline in `head` to avoid FOUC
if (localStorage.getItem('color-theme') === 'dark' || (!('color-theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
    document.documentElement.classList.add('dark');
} else {
    document.documentElement.classList.remove('dark');
}

// tryggvi 2024
const leafletMap = L;
let coasterMap;

function showMap(lat, lng) {
    const mapElement = document.getElementById('map');

    if (coasterMap) {
        coasterMap.remove();
    }

    coasterMap = leafletMap.map(mapElement).setView([lat, lng], 13);

    leafletMap.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
    }).addTo(coasterMap);

    leafletMap.marker([lat, lng]).addTo(coasterMap)
        .bindPopup('Location: ' + lat + ', ' + lng)
        .openPopup();
}

// Like button functionality
document.addEventListener('DOMContentLoaded', function () {
    const la = document.getElementById('lat');
    const lo = document.getElementById('lng');
    const lat = la.value; // Gets the content inside the div
    const lng = lo.value; // Gets the content inside the div
    showMap(lat, lng);


    const likeButton = document.createElement('button');
    likeButton.textContent = "Like";
    likeButton.className = "bg-blue-500 text-white px-4 py-2 rounded";
    likeButton.style.marginTop = "20px";

    const likeContainer = document.createElement('div');
    likeContainer.className = "flex justify-center";
    likeContainer.appendChild(likeButton);
    document.body.appendChild(likeContainer);

    const hasLiked = localStorage.getItem('hasLiked') === 'true';

    if (hasLiked) {
        likeButton.textContent = "Liked!";
        likeButton.disabled = true;
        likeButton.classList.add('opacity-50', 'cursor-not-allowed');
    }

    likeButton.addEventListener('click', function () {
        if (!hasLiked) {
            localStorage.setItem('hasLiked', 'true');
            likeButton.textContent = "Liked!";
            likeButton.disabled = true;
            likeButton.classList.add('opacity-50', 'cursor-not-allowed');
        }
    });
});
