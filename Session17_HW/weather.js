const input = document.querySelector('#city')
const button = document.querySelector('#submit')
const weatherBox = document.querySelector('#weatherBox')

const API_KEY_s = "145c78fe435fff0bc286b8df04224f3b";

button.addEventListener('click', async()=>{
  //input의 값을 가져와서 도시 이름으로 url에 넣는다.
  
  const city = input.value;
  //현재 날씨
  try {

    const API_KEY_f = "09348b9ebe4e3faf837f322704586250";
const future = await axios.get(`https://api.openweathermap.org/data/2.5/forecast?q=${city}&appid=${API_KEY_f}`);
console.log(future);
console.log(city);

//five day-three hour forecast data
//날짜, 도시명, 아이콘, 날씨(main), 최고기온, 최저기온
class forecast {
  constructor(time) { //생성자
    this.date = future.data.list[time].dt_txt.substring(0,10);
    this.name = future.data.city['name'];
    this.icon = future.data.list[time].weather[0].icon;
    this.main = future.data.list[time].weather[0].main;
    this.temp_max = Math.round(future.data.list[time].main.temp_max-273.15);
    this.temp_min = Math.round(future.data.list[time].main.temp_min-273.15);
  }
}


const day_0 = new forecast(2);
const day_1 = new forecast(10);
const day_2 = new forecast(18);
const day_3 = new forecast(26);
const day_4 = new forecast(34);
console.log(day_0.date);
const days = [day_0, day_1, day_2, day_3, day_4];
console.log(days[0].name);

let inner = ``

for (let i=0;i<5;i++) {
  inner += `
  <div class="day_box">
    <div class="date">${days[i].date}</div>
    <div class="name">${days[i].name}</div>
    <img class="icon" src="http://openweathermap.org/img/w/${days[i].icon}.png">
    <div class="main">${days[i].main}</div>
    <div class="temp_max">${days[i].temp_max}°C</div>
    <div class="temp_min">${days[i].temp_min}°C</div>
  </div>`;
}


  weatherBox.innerHTML = inner;

  let back = document.querySelector('body');

  console.log(day_0.main);

  switch(day_0.main) {
    case 'Clear':
      back.style.backgroundImage = "url(./background_images/clear.jpg)";
      back.classList.add('body_back'); 
      break;
    case 'Clouds':
      back.style.backgroundImage = "url(./background_images/clouds.jpg)";
      back.classList.add('body_back'); 
      break;
    case 'Rain':
      back.style.backgroundImage = "url(./background_images/rain.jpg)";
      back.classList.add('body_back'); 
      break;
    case 'Snow':
      back.style.backgroundImage = "url(./background_images/snow.jpg)";
      back.classList.add('body_back'); 
      break;
  }

  }
catch (error) {
  console.log(error);
}


//     back.style.backgroundImage = "url(./background_images/clear.jpg)";


//   case 'Clouds':
//     back.style.backgroundImage = "url(./background_images/clear.jpg)";

//   case 'Rain':

//   case 'Snow':


// }
});
//   const current = await axios.get(`https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${API_KEY_s}`);

//   console.log(current);

//   const {main, icon} = current.data.weather[0];
//   // const temp = Math.round(current.data.main.temp - 273.15);
//   const name = current.data.name;
//   const temp_max = Math.round(current.data.main.temp_max - 273.15);
//   const temp_min = Math.round(current.data.main.temp_min - 273.15);


//   weatherBox.innerHTML = `<div class="name">${name}</div>
//   <img class="icon" src="http://openweathermap.org/img/w/${icon}.png">
//   <div class="main">${main}</div>
//   <div class="temp_max">${temp_max}°C</div>
//   <div class="temp_min">${temp_min}°C</div>`;
// } 
// /* <div class="description">${description}</div>
//   <div class="temp">${temp}°C</div> */













