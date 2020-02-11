let usaCoords = [39.8283, -98.5795];
let mapZoomLevel = 2.5;

// Create the createMap function
function createMap(earthquakes) {
    let map = L.map('map').setView(usaCoords, mapZoomLevel);
    // Create the tile layer that will be the background of our map
    let lightMap = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    // Create a baseMaps object to hold the lightmap layer
    let baseMaps = {
        "Light Theme": lightMap
    };

    // Create an overlayMaps object to hold the earthquakes layer
    let overlayMaps = {
        "Earthquakes": earthquakes
    };

    lightMap.addTo(map);
    earthquakes.addTo(map);

    // Create a layer control, pass in the baseMaps and overlayMaps. Add the layer control to the map
    //   L.control.layers(baseMaps, overlayMaps, {
    //     collapsed: false
    //   }).addTo(map);
}
// Create the createMarkers function
function createMarkers(response) {
    // Pull the "features" property off of response.data
    let quakes = response.features;

    // Initialize an array to hold quake markers
    let quakeMarkers = [];


    // Loop through the quakes array
    // For each quake, create a marker and bind a popup with the quake's name, magnitude, and depth
    for (let index = 0; index < quakes.length; index++) {
        let quake = quakes[index];
        

        // Add the marker to the quakeMarkers array
        let quakeMarker = L.marker([quake.geometry.coordinates[1], quake.geometry.coordinates[0]], {
            icon: L.divIcon({
                html: '<i class="fa fa-exclamation-triangle" style="color: red"></i>',
                iconSize: [20, 20],
                className: 'myDivIcon'
            })
        }).bindTooltip("<div class='popup'><h2>" + quake.properties.place + "</h2>"
            + "<h3> Magnitude: " + quake.properties.mag
            + "<br> Depth of Epicenter: " + quake.geometry.coordinates[2]
            + "<br> Time: " + new Date(quake.properties.time)
            + "</h3></div>");

        quakeMarkers.push(quakeMarker);
    }
    // Create a layer group made from the quake markers array, pass it into the createMap function
    createMap(L.layerGroup(quakeMarkers));
}
// Perform an API call to the Earthquake Notification Service API to get quake information. Call createMarkers when complete
d3.json("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_week.geojson", createMarkers);