from clients.weather import get_weather
from clients.rates import get_rate
from processing.preprocessing import check_temp
from processing.preprocessing import check_curr

def build_city_summary(city, currency="USD"):
    weather = get_weather(city)

    rate = get_rate(currency)

    curr = {
        "currency": currency,
        "rate_to_rub": rate
    }

    temp = check_temp(weather)
    curr = check_curr(curr)

    return {
        "city": city,
        "weather": temp,
        "rates": curr
    }
