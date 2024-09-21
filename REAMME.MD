# Kano Weather Report Application

This Python application fetches and displays the current weather report for Kano, Nigeria using the OpenWeatherMap API.

## Features

- Real-time weather data for Kano, Nigeria
- Displays various weather metrics including temperature, humidity, wind speed, and more
- Converts temperature from Kelvin to Celsius
- Error handling for API requests
- Uses environment variables for secure API key storage

## Requirements

- Python 3.6+
- `requests` library
- `python-dotenv` library

## Installation

1. Clone this repository or download the script.
2. Install the required libraries:

```
pip install requests python-dotenv
```

3. Sign up for a free API key at [OpenWeatherMap](https://openweathermap.org/api).
4. Create a `.env` file in the same directory as the script with the following content:

```
OPENWEATHERMAP_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your actual OpenWeatherMap API key.

## Usage

Run the script from the command line:

```
python kano_weather_app.py
```

The application will display the current weather report for Kano, Nigeria in your console.

## Sample Output

```
=== Weather Report for Kano, Nigeria ===
Date and Time: 2024-09-22 15:30:45
Weather: Clear (clear sky)
Temperature: 32.5°C
Feels Like: 31.2°C
Min Temperature: 32.5°C
Max Temperature: 32.5°C
Humidity: 12%
Pressure: 1015 hPa
Wind Speed: 3.6 m/s
Wind Direction: 90°
=====================================
```

## Error Handling

The application includes error handling for API requests and will display appropriate error messages if it fails to fetch weather data.

## Customization

To change the city or country, modify the `CITY` variable in the script. For example:

```python
CITY = "Lagos,NG"
```

## Contributing

Contributions to this project are welcome. Feel free to fork the repository and submit pull requests, or open issues for any bugs or feature requests.

## License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).