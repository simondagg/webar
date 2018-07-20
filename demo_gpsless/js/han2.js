var front = false;

var constraints = { video: { facingMode: (front ? "user" : "environment"), width: { min: 1024, ideal: 1088, max: 4032 },
    height: { min: 776, ideal: 2020, max: 3024 } } };
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
        //ggggggggggggggggggggggggggggggggggggggggggggggg
        var camera= document.getElementById('camera');
        
        camera.object3D.position.set(latitude,0,longitude);
        
        document.getElementById('miku').object3D.position.set(camera.object3D.position.x+3,0, camera.object3D.position.z+3);

    }
    navigator.geolocation.getCurrentPosition(success, error)
}
setInterval(getgps, 3000);
