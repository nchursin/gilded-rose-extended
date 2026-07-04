# -*- coding: utf-8 -*-
from datetime import datetime, timedelta

import pytest

from gilded_rose import Receipt
from tests.testables import thursdayDatetime


@pytest.fixture
def tomorrow(today):
    return today + timedelta(days=1)

@pytest.fixture
def today():
    return datetime.today()

@pytest.fixture
def weekday_21_days_ago():
    return thursdayDatetime.today() - timedelta(days=21)

@pytest.fixture
def weekday_22_days_ago():
    return thursdayDatetime.today() - timedelta(days=22)

@pytest.fixture
def weekday_23_days_ago():
    return thursdayDatetime.today() - timedelta(days=23)

@pytest.fixture
def weekday_29_days_ago():
    return thursdayDatetime.today() - timedelta(days=29)

@pytest.fixture
def weekday_30_days_ago():
    return thursdayDatetime.today() - timedelta(days=30)

@pytest.fixture
def weekday_119_days_ago():
    return thursdayDatetime.today() - timedelta(days=119)

@pytest.fixture
def receipt_with_9_days_left(weekday_21_days_ago):
    return Receipt("Elixir of the Mongoose", "Rexxar", weekday_21_days_ago)

@pytest.fixture
def receipt_with_8_days_left(weekday_22_days_ago):
    return Receipt("Elixir of the Mongoose", "Rexxar", weekday_22_days_ago)

@pytest.fixture
def receipt_with_1_day_left(weekday_29_days_ago):
    return Receipt("Elixir of the Mongoose", "Rexxar", weekday_29_days_ago)

@pytest.fixture
def receipt_with_1_day_left_before_purge(weekday_119_days_ago):
    return Receipt("Elixir of the Mongoose", "Rexxar", weekday_119_days_ago)

@pytest.fixture
def receipt_from_today(today):
    return Receipt("Elixir of the Mongoose", "Rexxar", today)
