// script.js
API_KEY = "6f17bce624f94d769b279d0b8f61bc39"
// script.js

// script.js

var map = L.map('map-container').setView([0, 0], 2); // Set the initial view with a global scope

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
}).addTo(map);

// Function to add a marker for a place based on its name
function addMarkerForPlace(placeName) {
    // Use a geocoding service to obtain the latitude and longitude for the given placeName
    // Replace 'YOUR_API_KEY' with your actual API key for the chosen geocoding service
    var geocodingServiceURL = `https://api.opencagedata.com/geocode/v1/json?q=${encodeURIComponent(placeName)}&key=${API_KEY}`;
    
    fetch(geocodingServiceURL)
        .then(response => response.json())
        .then(data => {
            if (data.results.length > 0) {
                var coordinates = data.results[0].geometry;
                var marker = L.marker([coordinates.lat, coordinates.lng]).addTo(map);
                marker.bindPopup(placeName);
                map.setView([coordinates.lat, coordinates.lng], 10); // Adjust the view to the place's location
            } else {
                alert("Place not found. Please enter a valid place name.");
            }
        })
        .catch(error => {
            console.error("Error fetching geocoding data: ", error);
        });
}

// Example usage: Add a marker for a place based on its name
var placeNameInput = prompt("Enter the name of a place:");
if (placeNameInput) {
    addMarkerForPlace(placeNameInput);
}
