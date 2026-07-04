from gilded_rose import Item, GildedRose, Receipt
from datetime import datetime, timedelta

from tests.testables import thursdayDatetime, saturdayDatetime

class TestBoughtOnWeekday:
    def test_receipt_valid(self):
        receipt = Receipt("Elixir of the Mongoose", "Rexxar", thursdayDatetime.today())

        assert receipt.status == "valid"

    def test_receipt_valid_until_23_day_when_bought_on_weekday(self):
        receipt = Receipt("Elixir of the Mongoose", "Rexxar", thursdayDatetime.today() - timedelta(days=22))

        assert receipt.status == "valid"

    def test_receipt_expiring_soon_on_day_23_when_bought_on_weekday(self):
        receipt = Receipt("Elixir of the Mongoose", "Rexxar", thursdayDatetime.today() - timedelta(days=23))

        assert receipt.status == "expiring_soon"

    def test_receipt_expiring_soon_until_day_30_when_bought_on_weekday(self):
        receipt = Receipt("Elixir of the Mongoose", "Rexxar", thursdayDatetime.today() - timedelta(days=29))

        assert receipt.status == "expiring_soon"

    def test_receipt_archived_on_day_30_when_bought_on_weekday(self):
        receipt = Receipt("Elixir of the Mongoose", "Rexxar", thursdayDatetime.today() - timedelta(days=30))

        assert receipt.status == "archived"

    def test_receipt_archived_till_day_120(self):
        receipt = Receipt("Elixir of the Mongoose", "Rexxar", thursdayDatetime.today() - timedelta(days=119))

        assert receipt.status == "archived"

    def test_receipt_purged_on_day_120(self):
        receipt = Receipt("Elixir of the Mongoose", "Rexxar", thursdayDatetime.today() - timedelta(days=120))

        assert receipt.status == "purged"

class TestBoughtOnWeekend:
    def test_receipt_valid(self):
        receipt = Receipt("Elixir of the Mongoose", "Rexxar", saturdayDatetime.today())

        assert receipt.status == "valid"

    def test_receipt_valid_until_7_day_when_bought_on_weekend(self):
        receipt = Receipt("Elixir of the Mongoose", "Rexxar", saturdayDatetime.today() - timedelta(days=6))

        assert receipt.status == "valid"

    def test_receipt_expiring_soon_on_day_7_when_bought_on_weekend(self):
        receipt = Receipt("Elixir of the Mongoose", "Rexxar", saturdayDatetime.today() - timedelta(days=7))

        assert receipt.status == "expiring_soon"

    def test_receipt_expiring_soon_until_day_14_when_bought_on_weekend(self):
        receipt = Receipt("Elixir of the Mongoose", "Rexxar", saturdayDatetime.today() - timedelta(days=13))

        assert receipt.status == "expiring_soon"

    def test_receipt_archived_on_day_14_when_bought_on_weekend(self):
        receipt = Receipt("Elixir of the Mongoose", "Rexxar", saturdayDatetime.today() - timedelta(days=14))

        assert receipt.status == "archived"

    def test_receipt_archived_till_day_104(self):
        receipt = Receipt("Elixir of the Mongoose", "Rexxar", saturdayDatetime.today() - timedelta(days=103))

        assert receipt.status == "archived"

    def test_receipt_purged_on_day_104(self):
        receipt = Receipt("Elixir of the Mongoose", "Rexxar", saturdayDatetime.today() - timedelta(days=104))

        assert receipt.status == "purged"

