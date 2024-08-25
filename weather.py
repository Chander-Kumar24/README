import requests

# I have removed the api and you use your own api
API_KEY = 'Your api here'
BASE_URL = 'https://www.weatherapi.com/my/'

def fetch_weather(location):
    """Fetch the weather information for a given location."""
    params = {
        'q': location,
        'appid': API_KEY,
        'units': 'metric'  
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  

        data = response.json()
        if data['cod'] != 200:
            raise ValueError(data.get('message', 'Error fetching weather data'))

        weather = {
            'location': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed']
        }

        return weather

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
    except ValueError as e:
        print(f"Value error: {e}")
    except KeyError as e:
        print(f"Key error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def display_weather(weather):
    """Display the weather information."""
    if not weather:
        print("No weather information available.")
        return

    print(f"Location: {weather['location']}")
    print(f"Temperature: {weather['temperature']}°C")
    print(f"Description: {weather['description']}")
    print(f"Humidity: {weather['humidity']}%")
    print(f"Wind Speed: {weather['wind_speed']} m/s")

def main():
    """Main function to run the Weather Information App."""
    while True:
        location = input("Enter a location (or type 'exit' to quit): ").strip()
        if location.lower() == 'exit':
            print("Exiting...")
            break

        weather = fetch_weather(location)
        display_weather(weather)

if __name__ == "__main__":
    main()
