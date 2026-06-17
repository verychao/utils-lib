import pytest
from utils.math_utils import clamp, round_to, percentage


class TestClamp:
    def test_value_above_hi(self):
        assert clamp(15, 0, 10) == 10

    def test_value_below_lo(self):
        assert clamp(-5, 0, 10) == 0

    def test_value_in_range(self):
        assert clamp(5, 0, 10) == 5

    def test_value_at_lo(self):
        assert clamp(0, 0, 10) == 0

    def test_value_at_hi(self):
        assert clamp(10, 0, 10) == 10

    def test_lo_equals_hi(self):
        assert clamp(3, 5, 5) == 5

    def test_lo_greater_than_hi_raises(self):
        with pytest.raises(ValueError):
            clamp(5, 10, 0)


class TestRoundTo:
    def test_basic_round(self):
        assert round_to(3.14159, 2) == 3.14

    def test_zero_decimals(self):
        assert round_to(3.7, 0) == 4.0

    def test_negative_decimals_raises(self):
        with pytest.raises(ValueError):
            round_to(3.14, -1)

    def test_exact_value(self):
        assert round_to(1.5, 1) == 1.5


class TestPercentage:
    def test_basic(self):
        assert percentage(1, 3, 2) == 33.33

    def test_100_percent(self):
        assert percentage(5, 5, 2) == 100.0

    def test_zero_total_raises(self):
        with pytest.raises(ZeroDivisionError):
            percentage(1, 0)

    def test_default_decimals(self):
        assert percentage(1, 4) == 25.0
