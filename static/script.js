// async function getWeather() {
//   const cityName = document.getElementById("city").value;
//   const apiKey = "YOUR_OPENWEATHERMAP_API_KEY"; // Replace with your actual API key
//   const url = `https://api.openweathermap.org/data/2.5/weather?q=${cityName}&appid=${apiKey}&units=metric`;

//   try {
//     const response = await fetch(url);
//     const data = await response.json();

//     if (data.cod === 200) {
//       const weatherData = data.main;
//       const weatherConditions = data.weather[0].description;
//       const windSpeed = data.wind.speed;
//       const humidity = weatherData.humidity;
//       const temperature = weatherData.temp;
//       const icon = data.weather[0].icon;

//       document.getElementById(
//         "weather-icon"
//       ).src = `http://openweathermap.org/img/wn/${icon}.png`;
//       document.getElementById("weather-icon").style.display = "block";
//       document.getElementById("temp-div").innerHTML = `<p>${temperature}°C</p>`;
//       document.getElementById("weather-info").innerHTML = `
//                 <p>Conditions: ${weatherConditions}</p>
//                 <p>Wind Speed: ${windSpeed} m/s</p>
//                 <p>Humidity: ${humidity}%</p>
//             `;

//       // Optionally, you can display hourly forecast
//       // This part can be expanded based on the OpenWeather API response
//     } else {
//       alert("City not found!");
//     }
//   } catch (error) {
//     console.error("Error fetching weather data:", error);
//   }
// }
