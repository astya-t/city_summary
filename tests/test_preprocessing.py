from processing.preprocessing import check_temp
from processing.preprocessing import check_curr


def test_check_temp_below_zero():
    weather = {"temp_c": -13}

    result = check_temp(weather)

    assert result["warm_clothes"] is True


def test_check_temp_above_zero():
    weather = {"temp_c": 11}

    result = check_temp(weather)

    assert result["warm_clothes"] is False


def test_check_curr_above_100():
    rates = {
        "currency": "USD",
        "rate_to_rub": 110
    }

    result = check_curr(rates)

    assert result["expensive"] is True


def test_check_curr_below_100():
    rates = {
        "currency": "USD",
        "rate_to_rub": 70
    }

    result = check_curr(rates)

    assert result["expensive"] is False