const getRandomHexaColor = () => {
    const hexa = '0123456789abcdef';
    var color = '#';
    for (var i=0; i<6; i++) {
        color += hexa[Math.floor(Math.random() * 16)];
    }
    return color;
    
};

setInterval(() => { 
    document.querySelector('body').style.backgroundColor = 
    getRandomHexaColor();
}, 100);

const clockContent = document.querySelector('.now');

const getCurrentTime = () => {
    const date = new Date();
    var year = date.getFullYear();
    var month = date.getMonth()+1;
    var day = date.getDate();
    var hour = date.getHours();
    var minutes = date.getMinutes();
    var seconds = date.getSeconds();
    console.log(date);

    month = (month < 10) ? '0' + month : month;
    day = (day < 10) ? '0' + day : day;
    hour = (hour < 10) ? '0' + hour : hour;
    minutes = (minutes < 10) ? '0' + minutes : minutes;
    seconds = (minutes < 10) ? '0' + seconds : seconds;
    

    clockContent.innerText = `${year}년 ${month}월 ${day}일 ${hour}시 ${minutes}분 ${seconds}초`;
};

const initClock = () => {
    getCurrentTime();
    setInterval(getCurrentTime, 1000);
};

initClock();

