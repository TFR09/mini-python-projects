import requests
from time import sleep

API_KEY = "4b13b761e0d3d67372d2e5d7e54195d3"
URL = "https://api.openweathermap.org/data/2.5/weather"

def main():
    while True:
        city = input("Enter city to get weather data: ")
        get_weather_info(city)

        r = input("Press enter to continue or type anything to end > ")
        print()
        if r != "":
            break

    print("Thank you for using this program!")

def get_weather_info(city):
    data = requests.get(f"{URL}?q={city}&appid={API_KEY}&units=metric")

    if data.ok:
        data = data.json()
        weather = data["weather"][0]["description"]
        temperature = round(data["main"]["temp"], 2)
        temperature_percieved = round(data["main"]["feels_like"], 2)
        sleep(1)
        print(f"The weather in {city} is {weather}")
        sleep(1)
        print(f"The temperature is {temperature}℃  but feels like {temperature_percieved}℃\n")
    else:
        print("Error getting data!")

if __name__ == "__main__":
    main()