# Real-Time AQI and Weather Monitoring System

## Overview

This project is a real-time Air Quality Index (AQI) and weather monitoring application that retrieves live environmental data using external APIs. It provides users with key information such as temperature, air quality levels, humidity, and other atmospheric conditions for a selected city.

## Features

* Real-time weather data retrieval
* Air Quality Index (AQI) monitoring
* City-based search functionality
* Display of temperature, humidity, and wind details
* Integration with external APIs
* Responsive and user-friendly interface

## Tech Stack

### Frontend

* HTML
* CSS
* JavaScript

### APIs

* OpenWeatherMap API
* Air Quality API

## Project Structure

```
Real-Time-AQI-Project/
│── index.html
│── style.css
│── script.js
│── assets/
│── README.md
```

## Working Principle

1. The user inputs a city name
2. The application sends a request to external weather and AQI APIs
3. The APIs return data in JSON format
4. The application processes the data and extracts relevant fields
5. The processed information is displayed on the user interface

---

## Setup Instructions

1. Clone the repository:

```
git clone https://github.com/Khushali-Alt/Real-Time-AQI-Project.git
```

2. Navigate to the project directory:

```
cd Real-Time-AQI-Project
```

3. Open the `index.html` file in a web browser

## API Configuration

To run this project, an API key is required.

1. Visit https://openweathermap.org/ and create an account
2. Generate an API key
3. Replace the placeholder in the code:

```javascript
const API_KEY = "YOUR_API_KEY";
```

## Learning Outcomes

* Understanding of API integration
* Handling and parsing JSON data
* Use of asynchronous JavaScript (fetch/async-await)
* Structuring a real-world frontend project

## Future Enhancements

* Add geolocation-based weather detection
* Improve UI responsiveness across devices
* Include graphical representation of AQI trends
* Implement dark mode

## Author

Khushali Tiwari

## License

This project is open-source and available for educational purposes.
