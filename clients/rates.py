from clients.http_client import get_json


class RateError(Exception):
    pass


class CurrencyNotFoundError(RateError):
    pass


def get_rate(currency):
    try:
        url = f"https://api.frankfurter.dev/v2/rate/{currency}/RUB"

        data = get_json(url)

        if not isinstance(data, dict):
            raise ValueError(
                "Invalid response format: expected a dictionary"
            )

        if "rate" not in data:
            raise CurrencyNotFoundError(
                f"Валюта не найдена: {currency}"
            )

        if not isinstance(data["rate"], (int, float)):
            raise ValueError(
                "Invalid response: 'rate' value is not a number"
            )

        return data["rate"]

    except CurrencyNotFoundError:
        raise

    except Exception as error:
        if "422 Client Error" in str(error):
            raise CurrencyNotFoundError(
                f"Валюта не найдена: {currency}"
            )

        raise RateError(
            f"Не удалось получить курс валюты: {error}"
        )