var front = false;

var constraints = { video: { facingMode: (front ? "user" : "environment"), width: 1920, height: 1080 } };
navigator.mediaDevices.getUserMedia(constraints)
    .then(function (mediaStream) {
        var video = document.querySelector('video');
        video.srcObject = mediaStream;
        video.onloadedmetadata = function (e) {
            video.play();
        };
    })
    .catch(function (err) { console.log(err.name + ": " + err.message); });
function getgps() {

    function error() {
        alert("Unable to retrieve your location");
    }


    function success(position) {
        var latitude = position.coords.latitude * 100000;
        var longitude = position.coords.longitude * 100000;
        var coordinate = latitude.toString() + " 0 " + longitude.toString();
        document.getElementById('camera').setAttribute('position', coordinate);
        var mikucoordinate = (latitude+3).toString() + " 0 " + (longitude+3).toString();
        document.getElementById('miku').setAttribute('position', mikucoordinate);

    }
    navigator.geolocation.getCurrentPosition(success, error)
}
setInterval(getgps, 3000);