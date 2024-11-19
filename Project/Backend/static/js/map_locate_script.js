function getLocation() {
	setBuffering(true);
	if (navigator.geolocation) {
		navigator.geolocation.getCurrentPosition(
			(position) => {
				setPosition(position);
			},
			(error) => {
				alert(error.message);
			}
		);
	} else {
		alert("geolocation unavailable");
	}
}

function setPosition(position) {
	map.panTo(new L.LatLng(position.coords.latitude, position.coords.longitude));
	setBuffering(false);
}

function setBuffering(on) {
	let map_div = document.getElementById("map");
	if (on) {
		map_div.style.filter = "blur(3px)";
	} else {
		map_div.style.filter = "";
	}
}
