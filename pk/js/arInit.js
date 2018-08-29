document.getElementById("arCam").innerHTML='<video id="video" autoplay></video>';
document.getElementById("vrScene").innerHTML='<a-scene id="scene" vr-mode-ui="enabled: false"><a-camera id="camera" position="0 0 0"></a-camera><a-sphere visible="true" id="ball" position="0 0 -1" radius="0.05"></a-sphere><a-assets id="assets"></a-assets></a-scene>';

//video id="video"
//a-scene id="scene"
//a-camera id="camera"
//a-assets id="assets"
let front = false;
let constraints = { video: { facingMode: (front ? "user" : "environment"), width: 800, height: 450 } };
navigator.mediaDevices.getUserMedia(constraints)
    .then(function (mediaStream) {
        var video = document.querySelector('video');
        video.srcObject = mediaStream;
        video.onloadedmetadata = function (e) {
            video.play();
        };
    })
    .catch(function (err) { console.log(err.name + ": " + err.message); });

    //光標位置
    window.addEventListener('deviceorientation', function () {
        var camera=document.getElementById("camera");
        var x = camera.object3D.position.x, z = camera.object3D.position.z;
        var y = 0;
        var r_y = camera.object3D.rotation.y;// theta/180*pi   
        var r_x = camera.object3D.rotation.x;
        if (r_y == 0) {
            z = z - 5;
        }
        else {
            z = z - 5 * Math.cos(r_y);
            x = x - 5 * Math.sin(r_y);
        }
        y = y + 5 * Math.sin(r_x);
        var ball = document.getElementById("ball");
        ball.setAttribute("position", { x: x, y: y, z: z });
    });
   

