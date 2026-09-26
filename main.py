import argparse
import sys

from processing.service import build_city_summary
from clients.weather import WeatherError, CityNotFoundError
from clients.rates import RateError, CurrencyNotFoundError


parser = argparse.ArgumentParser()

parser.add_argument("--city", required=True)
parser.add_argument("--currency", default="USD")

args = parser.parse_args()


try:
    result = build_city_summary(args.city, args.currency)

except CityNotFoundError as error:
    print(f"Ошибка: {error}")
    sys.exit(3)

except CurrencyNotFoundError as error:
    print(f"Ошибка: {error}")
    sys.exit(3)

except WeatherError as error:
    print(f"Ошибка погоды: {error}")
    sys.exit(4)

except RateError as error:
    print(f"Ошибка курса валют: {error}")
    sys.exit(4)


print(f"Город: {result['city']}")
print(f"Погода: {result['weather']['temp_c']}°C")

if result["weather"]["warm_clothes"]:
    print("Тёплая одежда: да")
else:
    print("Тёплая одежда: нет")

print(
    f"{result['rates']['currency']}→RUB: "
    f"{result['rates']['rate_to_rub']}"
)

if result["rates"]["expensive"]:
    print("Дорогой курс: да")
else:
    print("Дорогой курс: нет")


sys.exit(0)