from datetime import datetime

from gilded_rose import GildedRose

class thursdayDatetime(datetime):
    def __new__(cls, *args, **kwargs):
        return datetime.__new__(cls, *args, **kwargs)

    def weekday(self) -> int:
        return 4


class saturdayDatetime(datetime):
    def __new__(cls, *args, **kwargs):
        return datetime.__new__(cls, *args, **kwargs)

    def weekday(self) -> int:
        return 5

class TestableGildedRose(GildedRose):
    def __init__(self, items, receipts=None):
        super().__init__(items, receipts)
        self.current_date = datetime.now()

    def now(self):
        return self.current_date

    def update_quality_for_date(self, date):
        self.current_date = date
        return super().update_quality()
