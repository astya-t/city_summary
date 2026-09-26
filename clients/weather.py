from clients.http_client import get_json


class WeatherError(Exception):
    pass


def get_weather(city):
    try:
        url = (
            f"https://geocoding-api.open-meteo.com/v1/search"
            f"?name={city}&count=1"
        )

        data = get_json(url)

        results = data["results"][0]

        latitude = results["latitude"]
        longitude = results["longitude"]

        url = (
            f"https://api.open-meteo.com/v1/forecast"
            f"?latitude={latitude}"
            f"&longitude={longitude}"
            f"&current=temperature_2m"
        )

        data = get_json(url)

        temperature = data["current"]["temperature_2m"]

        return {
            "temp_c": temperature
        }

    except Exception as error:
        raise WeatherError(
            f"Не удалось получить данные о погоде: {error}"
        )