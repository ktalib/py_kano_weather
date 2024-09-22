import requests
import datetime
import os
from dotenv import load_dotenv
from colorama import init, Fore, Back, Style

# Initialize colorama
init(autoreset=True)

# Load environment variables from .env file
load_dotenv()

# OpenWeatherMap API configuration
API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")
CITY = "Kano,NG"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def get_weather_data():
    params = {
        "q": CITY,
        "appid": API_KEY,
    }
    
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"{Fore.RED}Error fetching weather data: {response.status_code}")
        return None

def display_weather_report(weather_data):
    if weather_data:
        main = weather_data['main']
        weather = weather_data['weather'][0]
        wind = weather_data['wind']
        
        print(f"\n{Back.BLUE}{Fore.WHITE}{Style.BRIGHT}=== Weather Report for Kano, Nigeria ==={Style.RESET_ALL}")
        print(f"{Fore.CYAN}Date and Time: {Fore.YELLOW}{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"{Fore.CYAN}Weather: {Fore.YELLOW}{weather['main']} ({weather['description']})")
        print(f"{Fore.CYAN}Temperature: {Fore.YELLOW}{kelvin_to_celsius(main['temp']):.1f}°C")
        print(f"{Fore.CYAN}Feels Like: {Fore.YELLOW}{kelvin_to_celsius(main['feels_like']):.1f}°C")
        print(f"{Fore.CYAN}Min Temperature: {Fore.YELLOW}{kelvin_to_celsius(main['temp_min']):.1f}°C")
        print(f"{Fore.CYAN}Max Temperature: {Fore.YELLOW}{kelvin_to_celsius(main['temp_max']):.1f}°C")
        print(f"{Fore.CYAN}Humidity: {Fore.YELLOW}{main['humidity']}%")
        print(f"{Fore.CYAN}Pressure: {Fore.YELLOW}{main['pressure']} hPa")
        print(f"{Fore.CYAN}Wind Speed: {Fore.YELLOW}{wind['speed']} m/s")
        print(f"{Fore.CYAN}Wind Direction: {Fore.YELLOW}{wind['deg']}°")
        if 'rain' in weather_data:
            print(f"{Fore.CYAN}Rainfall (last 1h): {Fore.YELLOW}{weather_data['rain'].get('1h', 0)} mm")
        print(f"{Back.BLUE}{Fore.WHITE}{Style.BRIGHT}====================================={Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}Unable to fetch weather data.")

def main():
    if not API_KEY:
        print(f"{Fore.RED}Error: OpenWeatherMap API key not found. Please set it in the .env file.")
        return
    
    weather_data = get_weather_data()
    display_weather_report(weather_data)

if __name__ == "__main__":
    main()