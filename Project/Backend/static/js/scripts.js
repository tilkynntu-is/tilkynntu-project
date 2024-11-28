// tryggvi 2024
const leafletMap = L;
let coasterMap;

function showMap(lat, lng) {
    const mapElement = document.getElementById('map');

    // Ensure the map container has dimensions
    mapElement.style.height = "100%"; // Ensure the container has height
    mapElement.style.width = "100%";  // Ensure the container has width
    
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
