# -*- coding: utf-8 -*-
from datetime import datetime, timedelta


class GildedRose(object):

    def __init__(self, items, receipts=None):
        self.items = items
        self.receipts = receipts if receipts is not None else []

    def update_quality(self):
        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.quality = item.quality - 1
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1
        for receipt in self.receipts:
            now = datetime.now()
            if now <= receipt.return_deadline:
                if (receipt.return_deadline - now).days < 7:
                    receipt.status = "expiring_soon"
                else:
                    receipt.status = "valid"
            else:
                if now <= receipt.return_deadline + timedelta(days=90):
                    receipt.status = "archived"
                else:
                    receipt.status = "purged"


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class Receipt:
    def __init__(self, item_name, customer_name, purchase_datetime):
        self.item_name = item_name
        self.customer_name = customer_name
        self.purchase_datetime = purchase_datetime
        if purchase_datetime.weekday() >= 5:
            self.return_deadline = purchase_datetime + timedelta(days=14)
        else:
            self.return_deadline = purchase_datetime + timedelta(days=30)
        if purchase_datetime.hour >= 18:
            self.return_deadline = self.return_deadline + timedelta(days=1)
        now = datetime.now()
        if now <= self.return_deadline:
            if (self.return_deadline - now).days < 7:
                self.status = "expiring_soon"
            else:
                self.status = "valid"
        else:
            if now <= self.return_deadline + timedelta(days=90):
                self.status = "archived"
            else:
                self.status = "purged"

    def __repr__(self):
        return "%s, %s, %s, %s" % (self.item_name, self.customer_name, self.return_deadline.strftime("%Y-%m-%d"), self.status)


def generate_receipt_report(receipts):
    print("===== Receipt Report [%s] =====" % datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    valid_count = 0
    expiring_count = 0
    archived_count = 0
    for receipt in receipts:
        if receipt.status == "valid":
            valid_count = valid_count + 1
        if receipt.status == "expiring_soon":
            expiring_count = expiring_count + 1
        if receipt.status == "archived":
            archived_count = archived_count + 1
    print("Valid: %d" % valid_count)
    print("Expiring soon: %d" % expiring_count)
    print("Archived: %d" % archived_count)
    print("")
    for receipt in receipts:
        if receipt.status != "purged":
            print(receipt)
