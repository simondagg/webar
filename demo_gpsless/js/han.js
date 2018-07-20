var front = false;

var constraints = { video: { facingMode: (front ? "user" : "environment"), width: 540, height: 1110 } };
navigator.mediaDevices.getUserMedia(constraints)
    .then(function (mediaStream) {
        var video = document.querySelector('video');
        video.srcObject = mediaStream;
        video.onloadedmetadata = function (e) {
            video.play();
        };
    })
    .catch(function (err) { console.log(err.name + ": " + err.message); });
