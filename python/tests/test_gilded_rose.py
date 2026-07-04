# -*- coding: utf-8 -*-
import pytest

from gilded_rose import Item, GildedRose

class TestNormalItems:
    def test_quality_decreases_by_1_per_day(self):
        gilded_rose = GildedRose([Item("Elixir of the Mongoose", sell_in=10, quality=20)])
        gilded_rose.update_quality()
        assert gilded_rose.items[0].quality == 19

    def test_sell_in_decreases_by_1_per_day(self):
        gilded_rose = GildedRose([Item("Elixir of the Mongoose", sell_in=10, quality=20)])
        gilded_rose.update_quality()
        assert gilded_rose.items[0].sell_in == 9

    def test_quality_decreases_twice_as_fast_after_sell_date(self):
        gilded_rose = GildedRose([Item("Elixir of the Mongoose", sell_in=0, quality=20)])
        gilded_rose.update_quality()
        assert gilded_rose.items[0].quality == 18

    def test_quality_never_goes_negative(self):
        gilded_rose = GildedRose([Item("Elixir of the Mongoose", sell_in=10, quality=0)])
        gilded_rose.update_quality()
        assert gilded_rose.items[0].quality == 0

    def test_quality_never_goes_negative_after_sell_date(self):
        gilded_rose = GildedRose([Item("Elixir of the Mongoose", sell_in=-1, quality=1)])
        gilded_rose.update_quality()
        assert gilded_rose.items[0].quality == 0

    def test_quality_never_exceeds_50(self):
        gilded_rose = GildedRose([Item("Elixir of the Mongoose", sell_in=10, quality=50)])
        gilded_rose.update_quality()
        assert gilded_rose.items[0].quality == 49


class TestAgedBrie:
    def test_quality_increases_by_1_per_day(self):
        gilded_rose = GildedRose([Item("Aged Brie", sell_in=10, quality=20)])
        gilded_rose.update_quality()
        assert gilded_rose.items[0].quality == 21

    def test_sell_in_decreases_by_1_per_day(self):
        gilded_rose = GildedRose([Item("Aged Brie", sell_in=10, quality=20)])
        gilded_rose.update_quality()
        assert gilded_rose.items[0].sell_in == 9

    def test_quality_increases_twice_as_fast_after_sell_date(self):
        gilded_rose = GildedRose([Item("Aged Brie", sell_in=0, quality=20)])
        gilded_rose.update_quality()
        assert gilded_rose.items[0].quality == 22

    def test_quality_capped_at_50(self):
        gilded_rose = GildedRose([Item("Aged Brie", sell_in=10, quality=50)])
        gilded_rose.update_quality()
        assert gilded_rose.items[0].quality == 50

    def test_quality_capped_at_50_after_sell_date(self):
        gilded_rose = GildedRose([Item("Aged Brie", sell_in=-1, quality=49)])
        gilded_rose.update_quality()
        assert gilded_rose.items[0].quality == 50


class TestSulfuras:
    def test_quality_never_changes(self):
        gilded_rose = GildedRose([Item("Sulfuras, Hand of Ragnaros", sell_in=0, quality=80)])
        gilded_rose.update_quality()
        assert gilded_rose.items[0].quality == 80

    def test_sell_in_never_changes(self):
        gilded_rose = GildedRose([Item("Sulfuras, Hand of Ragnaros", sell_in=0, quality=80)])
        gilded_rose.update_quality()
        assert gilded_rose.items[0].sell_in == 0

    def test_quality_never_changes_with_negative_sell_in(self):
        gilded_rose = GildedRose([Item("Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80)])
        gilded_rose.update_quality()
        assert gilded_rose.items[0].quality == 80


class TestBackstagePasses:
    def test_quality_increases_by_1_when_more_than_10_days(self):
        gilded_rose = GildedRose([Item("Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20)])
        gilded_rose.update_quality()
        assert gilded_rose.items[0].quality == 21

    def test_quality_increases_by_2_when_10_days_or_fewer(self):
        gilded_rose = GildedRose([Item("Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=20)])
        gilded_rose.update_quality()
        assert gilded_rose.items[0].quality == 22

    def test_quality_increases_by_2_when_6_days(self):
        gilded_rose = GildedRose([Item("Backstage passes to a TAFKAL80ETC concert", sell_in=6, quality=20)])
        gilded_rose.update_quality()
        assert gilded_rose.items[0].quality == 22

    def test_quality_increases_by_3_when_5_days_or_fewer(self):
        gilded_rose = GildedRose([Item("Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=20)])
        gilded_rose.update_quality()
        assert gilded_rose.items[0].quality == 23

    def test_quality_increases_by_3_when_1_day(self):
        gilded_rose = GildedRose([Item("Backstage passes to a TAFKAL80ETC concert", sell_in=1, quality=20)])
        gilded_rose.update_quality()
        assert gilded_rose.items[0].quality == 23

    def test_quality_drops_to_0_after_concert(self):
        gilded_rose = GildedRose([Item("Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=40)])
        gilded_rose.update_quality()
        assert gilded_rose.items[0].quality == 0

    def test_quality_capped_at_50(self):
        gilded_rose = GildedRose([Item("Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49)])
        gilded_rose.update_quality()
        assert gilded_rose.items[0].quality == 50

    def test_sell_in_decreases_by_1_per_day(self):
        gilded_rose = GildedRose([Item("Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=20)])
        gilded_rose.update_quality()
        assert gilded_rose.items[0].sell_in == 9
