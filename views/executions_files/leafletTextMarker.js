// see http://leaflet.uservoice.com/forums/150880-ideas-and-suggestions-for-leaflet/suggestions/2720350-number-the-markers for the source of this L.Icon override
var LeafMarkerText = L.Icon.extend({ 
	markerText: '', // 
	initialize: function (markerText) { // use number has parameter instead of iconUrl 
		if (markerText) { 
			this.markerText = markerText; 
		} 
	}, 
    popupAnchor: new L.Point(0, 0),
	_createIcon: function () {// override Icon creation to replace 
		var t = document.createElement('div');
		t.className = "leaflet-marker-icon leaflet-marker-text";
		t.innerHTML = this.markerText;
		return t;
	}, 
}); 

/* implement with something like...

var textMarkerLayer = new L.GeoJSON(null, {
    pointToLayer: function (latlng) {
    	var myIconText = new LeafMarkerText("hi");
        return new L.Marker(latlng, {icon : myIconText});
    }
});

*/
