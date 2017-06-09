/*$(document).ready(*/function myMap() {
    var mapCanvas = document.getElementById("map");
    var mapOptions = {
        center: new google.maps.LatLng(47.21, -1.55),
        zoom: 10
    };
    var map = new google.maps.Map(mapCanvas, mapOptions);
}//);
