from src.date_utils import workday
from datetime import date


def test_workday():
    assert workday(date(2021, 9, 16), -10) == date(2021, 9, 2)
    assert workday(date(2021, 9, 16), -5) == date(2021, 9, 9)
    assert workday(date(2021, 9, 16), -1) == date(2021, 9, 15)
    assert workday(date(2021, 9, 16), 1) == date(2021, 9, 17)
    assert workday(date(2021, 9, 16), 3) == date(2021, 9, 21)
    assert workday(date(2021, 9, 16), 10) == date(2021, 9, 30)