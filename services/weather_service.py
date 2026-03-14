import requests


def get_weather():

    try:

        location = requests.get("https://ipapi.co/json/").json()

        city = location["city"]

        weather = requests.get(
            f"https://wttr.in/{city}?format=%t+%C"
        ).text

        return f"🌦 {city} {weather}"

    except:

        return "Weather unavailable"