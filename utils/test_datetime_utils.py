from datetime import datetime, date
from utils.datetime_utils import format_date, days_between, is_weekday


def test_format_date_default():
    assert format_date(datetime(2024, 1, 5)) == "2024-01-05"


def test_format_date_custom():
    assert format_date(datetime(2024, 1, 5), "%d/%m/%Y") == "05/01/2024"


def test_days_between_positive():
    assert days_between(date(2024, 1, 1), date(2024, 1, 10)) == 9


def test_days_between_negative_direction():
    assert days_between(date(2024, 1, 10), date(2024, 1, 1)) == 9


def test_days_between_same():
    assert days_between(date(2024, 1, 1), date(2024, 1, 1)) == 0


def test_is_weekday_monday():
    assert is_weekday(date(2024, 1, 1)) is True  # Monday


def test_is_weekday_friday():
    assert is_weekday(date(2024, 1, 5)) is True  # Friday


def test_is_weekday_saturday():
    assert is_weekday(date(2024, 1, 6)) is False  # Saturday


def test_is_weekday_sunday():
    assert is_weekday(date(2024, 1, 7)) is False  # Sunday
