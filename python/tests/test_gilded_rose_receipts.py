# -*- coding: utf-8 -*-
from gilded_rose import GildedRose
from tests.testables import TestableGildedRose

def test_receipt_becomes_expiring_soon(receipt_with_8_days_left, tomorrow):
    gilded_rose = TestableGildedRose([], [receipt_with_8_days_left])

    gilded_rose.update_quality_for_date(tomorrow)

    assert receipt_with_8_days_left.status == "expiring_soon"

def test_receipt_becomes_archived(receipt_with_1_day_left, tomorrow):
    gilded_rose = TestableGildedRose([], [receipt_with_1_day_left])

    gilded_rose.update_quality_for_date(tomorrow)

    assert receipt_with_1_day_left.status == "archived"

def test_receipt_becomes_purged(receipt_with_1_day_left_before_purge, tomorrow):
    gilded_rose = TestableGildedRose([], [receipt_with_1_day_left_before_purge])

    gilded_rose.update_quality_for_date(tomorrow)

    assert receipt_with_1_day_left_before_purge.status == "purged"

def test_receipt_stays_valid(receipt_from_today, tomorrow):
    gilded_rose = TestableGildedRose([], [receipt_from_today])

    gilded_rose.update_quality_for_date(tomorrow)

    assert receipt_from_today.status == "valid"
