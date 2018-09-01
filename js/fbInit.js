var config = {
    apiKey: "AIzaSyCzaYpvOmLYeERBRCcO8M_e4ryAE57nLB8",
    authDomain: "fir-1-2b746.firebaseapp.com",
    databaseURL: "https://fir-1-2b746.firebaseio.com",
    projectId: "fir-1-2b746",
    storageBucket: "fir-1-2b746.appspot.com",
    messagingSenderId: "772658594851"
};
firebase.initializeApp(config);

var userID;

//-------------------接收Android資料--------------------
function currentUser(msg) {
    // 取得使用者ID
    userID = msg;

}

//var id;
//id = randomWord(false,10);
function randomWord(randomFlag, min, max) {
    var str = "",
        range = min,
        arr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];

    // 随机产生
    if (randomFlag) {
        range = Math.round(Math.random() * (max - min)) + min;
    }
    for (var i = 0; i < range; i++) {
        pos = Math.round(Math.random() * (arr.length - 1));
        str += arr[pos];
    }
    return str;
}

var updataObj = (dataArray) => {
    dataArray = [];
    var i = 0;
    var query = firebase.database().ref("Object").orderByKey();
    query.once("value")
        .then(function (snapshot) {
            snapshot.forEach(function (childSnapshot) {
                var key = childSnapshot.key;
                var childData = childSnapshot.val();
                dataArray.push(childData);
                dataArray[i] = Object.assign(dataArray[i], { objid: key });
                i = i + 1;
            });
        });
    return dataArray;
};