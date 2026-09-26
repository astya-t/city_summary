from clients.http_client import get_json


class RateError(Exception):
    pass


def get_rate(currency):
    try:
        url = f"https://api.frankfurter.dev/v2/rate/{currency}/RUB"

        data = get_json(url)

        if isinstance(data, dict):
            if "rate" in data:
                if isinstance(data["rate"], (int, float)):
                    return data["rate"]
                else:
                    raise ValueError(
                        "Invalid response: 'rate' value is not a number"
                    )
            else:
                raise ValueError(
                    "Invalid response: missing 'rate' key"
                )
        else:
            raise ValueError(
                "Invalid response format: expected a dictionary"
            )

    except Exception as error:
        raise RateError(
            f"Не удалось получить курс валюты: {error}"
        )