// see http://leaflet.cloudmade.com
var map = new L.Map('map');

map.setView(new L.LatLng(37, -95), 4);

//var cloudmadeUrl = 'http://{s}.tile.cloudmade.com/BC9A493B41014CAABB98F0471D759707/997/256/{z}/{x}/{y}.png', cloudmadeAttribution = 'Map data &copy; 2011 OpenStreetMap contributors, Imagery &copy; 2011 CloudMade', cloudmade = new L.TileLayer(cloudmadeUrl, {maxZoom: 18, attribution: cloudmadeAttribution});
//map.addLayer(cloudmade);

// see http://maps.stamen.com
var stamenLayer = new L.StamenTileLayer("watercolor");
map.addLayer(stamenLayer);

var geojsonMarkerOptions = {
    radius: 4,
    fillColor: "rgba(255,100,100,0.1)",
    color: "rgba(255,100,100,0.7)",
    weight: 1,
    opacity: 1,
    fillOpacity: 0.8
};

var geojsonLayer = new L.GeoJSON(null, {
    pointToLayer: function (latlng) {
		return new L.CircleMarker(latlng, geojsonMarkerOptions);
    }
});

geojsonLayer.on("featureparse", function (e) {
	if (e.properties && e.properties.County){
		e.layer.bindPopup(e.properties.County + ", " + e.properties.State 
			+ "<br>FIPS: " + e.properties.FIPS
			+ "<br>Executions: " + e.properties.Executions
		);
	}
    if (e.properties && e.properties.style && e.layer.setStyle) {
        e.layer.setStyle(e.properties.style);
    }
});

for (i=0; i < counties.length; i++) {
	var executions = counties[i].properties.Executions;
	var exColor = "#ffffff";
	var exO = "1.0";
	if (executions > 0) {
		exColor = "#d0d570";
	}
	if (executions > 1) {
		exColor = "#cfd642";
	}
	if (executions > 5) {
		exColor = "#ccd516";
	}
	if (executions > 10) {
		exColor = "#d5a216";
	}
	if (executions > 25) {
		exColor = "#d56016";
	}
	if (executions > 100) {
		exColor = "#ec1515";
	}
	counties[i].properties.style = { 
        weight: 1,
        color: "#eeeeee",
        opacity: 0.6,
        fillColor: exColor,
        fillOpacity: exO
	};
	geojsonLayer.addGeoJSON(counties[i]);
}

map.addLayer(geojsonLayer);

/*
var markerLocation = new L.LatLng(-84, 38),
	marker = new L.Marker(markerLocation);

map.addLayer(marker);
marker.bindPopup("<b>Hello world!</b><br />I am a popup.").openPopup();


var circleLocation = new L.LatLng(51.508, -0.11),
	circleOptions = {color: '#f03', opacity: 0.7},
	circle = new L.Circle(circleLocation, 500, circleOptions);

circle.bindPopup("I am a circle.");
map.addLayer(circle);


var p1 = new L.LatLng(51.509, -0.08),
	p2 = new L.LatLng(51.503, -0.06),
	p3 = new L.LatLng(51.51, -0.047),
	polygonPoints = [p1, p2, p3],
	polygon = new L.Polygon(polygonPoints);

polygon.bindPopup("I am a polygon.");
map.addLayer(polygon);

map.on('click', onMapClick);

var popup = new L.Popup();

function onMapClick(e) {
	var latlngStr = '(' + e.latlng.lat.toFixed(3) + ', ' + e.latlng.lng.toFixed(3) + ')';

	popup.setLatLng(e.latlng);
	popup.setContent("You clicked the map at " + latlngStr);
	map.openPopup(popup);
}
*/
