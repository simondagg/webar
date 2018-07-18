var front = false;

var constraints = { video: { facingMode: (front ? "user" : "environment"), width: 1280, height: 720 } };
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

    }
    navigator.geolocation.getCurrentPosition(success, error)
}
document.querySelector('a-box').addEventListener('collide', function (evt) {
    console.log('This A-Frame entity collided with another entity!');
  });
setInterval(getgps, 5000);
