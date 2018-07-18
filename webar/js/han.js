// Prefer camera resolution nearest to 1280x720.
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
                    .catch(function (err) { console.log(err.name + ": " + err.message); }); // always check for errors at the end.




                let scene, camera, render, geometry, material, cube;
                init();
                function init() {
                    //新增場景
                    scene = new THREE.Scene();



                    //新增相機
                    camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
                    camera.position.set(0, 0, 5);
                    camera.rotation.order = "YXZ";
                    window.addEventListener('deviceorientation', handleOrientation);
                    function handleOrientation(event) {
                        camera.rotation.x = event.beta * (Math.PI / 180);//上下
                        camera.rotation.y = event.gamma * (Math.PI / 180);//左右
                        camera.rotation.z = event.alpha * (Math.PI / 180);//垂直
                    }
                    //camera.updateProjectionMatrix();
                    //新增渲染
                    renderer = new THREE.WebGLRenderer({ alpha: true });
                    renderer.setClearColor(0x000000, 0);
                    renderer.setSize(window.innerWidth, window.innerHeight);
                    document.body.appendChild(renderer.domElement);
                    // LIGHT
                    light = new THREE.SpotLight(0xffffff)
                    light.position.set(3, 4, 8)
                    scene.add(light)
                    scene.add(new THREE.AmbientLight(0xaaaaaa, 0.3))

                    // GEOMERTRY
                    geometry = new THREE.BoxGeometry(1, 1, 1)

                    // MATERIAL
                    material = new THREE.MeshLambertMaterial({
                        color: 0xabcdef
                    })

                    // MESH
                    object = new THREE.Mesh(geometry, material)

                    scene.add(object)
                }

                function animate() {
                    requestAnimationFrame(animate);

                    renderer.render(scene, camera);
                }
                animate();
