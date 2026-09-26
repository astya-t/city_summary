def check_temp(weather):
    if weather["temp_c"] < 0:
        weather["warm_clothes"] = True
    else:
        weather["warm_clothes"] = False

    return weather

def check_curr(currency):
    if currency["rate_to_rub"] >100:
        currency["expensive"] = True
    else:
        currency["expensive"] = False

    return currency
