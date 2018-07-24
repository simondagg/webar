 //webcam
 var front = false;

 var constraints = { video: { facingMode: (front ? "user" : "environment"), width: 800, height: 450 } };
 navigator.mediaDevices.getUserMedia(constraints)
     .then(function (mediaStream) {
         var video = document.querySelector('video');
         video.srcObject = mediaStream;
         video.onloadedmetadata = function (e) {
             video.play();
         };
     })
     .catch(function (err) { console.log(err.name + ": " + err.message); });
 ///////////////////////////////////////////////////////////////////////////

 //put obj
 var scene = document.querySelector('a-scene');
 var camera = document.querySelector('a-camera');




 function putobj() {
     var x = camera.object3D.position.x, z = camera.object3D.position.z;
     var y = camera.object3D.rotation.y;// theta/180*pi         

     if (y == 0) {
         z = z - 5;
     }
     else {
         z = z - 5 * Math.cos(y);
         x = x - 5 * Math.sin(y);
     }
     var obj = document.createElement('a-box');
     //obj.setAttribute("id", "box");
     obj.setAttribute('color', '#4CC3D9');
     obj.setAttribute('position',{x: x, y: 0, z: z});
     scene.appendChild(obj);
 }
 /////////////////////////////////////////////////////////////////////////



//wale lock gps

//////////////////////////////////////////////////////////////////////////////////////  

//get gps
  function getgps() {

    function error() {
        alert("Unable to retrieve your location");
    }


    function success(position) {
        var latitude = position.coords.latitude * 100000;
        var longitude = position.coords.longitude * 100000;
     
        
        
        camera.object3D.position.set(longitude,0,latitude);
        
       

    }
    navigator.geolocation.getCurrentPosition(success, error)
}
setInterval(getgps, 100);

////////////////////////////////////////////////////////////////////////////////////////