from clients.http_client import get_json


class WeatherError(Exception):
    pass


class CityNotFoundError(WeatherError):
    pass


def get_weather(city):
    try:
        url = (
            f"https://geocoding-api.open-meteo.com/v1/search"
            f"?name={city}&count=1"
        )

        data = get_json(url)

        if not isinstance(data, dict):
            raise ValueError("Некорректный формат ответа геокодирования")

        if not data.get("results"):
            raise CityNotFoundError(f"Город не найден: {city}")

        if not isinstance(data["results"], list):
            raise ValueError("Поле 'results' должно быть списком")

        

        results = data["results"][0]

        if not isinstance(results, dict):
            raise ValueError("Некорректный формат данных о городе")

        if "latitude" not in results:
            raise ValueError("В данных города отсутствует 'latitude'")

        if "longitude" not in results:
            raise ValueError("В данных города отсутствует 'longitude'")

        latitude = results["latitude"]
        longitude = results["longitude"]

        url = (
            f"https://api.open-meteo.com/v1/forecast"
            f"?latitude={latitude}"
            f"&longitude={longitude}"
            f"&current=temperature_2m"
        )

        data = get_json(url)

        if not isinstance(data, dict):
            raise ValueError("Некорректный формат ответа прогноза")

        if "current" not in data:
            raise ValueError("В ответе отсутствует поле 'current'")

        if not isinstance(data["current"], dict):
            raise ValueError("Поле 'current' должно быть словарём")

        if "temperature_2m" not in data["current"]:
            raise ValueError(
                "В ответе отсутствует поле 'temperature_2m'"
            )

        temperature = data["current"]["temperature_2m"]

        if not isinstance(temperature, (int, float)):
            raise ValueError(
                "Температура должна быть числом"
            )

        return {
            "temp_c": temperature
        }

    except CityNotFoundError:
        raise

    except Exception as error:
        raise WeatherError(
            f"Не удалось получить данные о погоде: {error}"
        )