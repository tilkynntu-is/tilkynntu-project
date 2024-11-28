// testa eva js er connected
console.log("JavaScript file is successfully connected!");

    // On page load or when changing themes, best to add inline in `head` to avoid FOUC
    if (localStorage.getItem('color-theme') === 'dark' || (!('color-theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
        document.documentElement.classList.add('dark');
    } else {
        document.documentElement.classList.remove('dark')
    }


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

document.addEventListener('DOMContentLoaded', function () {
    showMap(40.1489, -74.4408);
});
