# -*- coding: utf-8 -*-


class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        # iterate through a list of items
        for item in self.items:
            self.update_item(item)
            self.cap_quality(item)

    def cap_quality(self, item):
        item.quality = min(item.quality, 50)
        item.quality = max(item.quality, 0)

    def update_item(self, item):
        if item.name == "Aged Brie":
            self.update_aged_brie(item)
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            self.update_backstage_pass(item)
        elif item.name != "Sulfuras, Hand of Ragnaros":
            self.update_normal_item(item)

    def update_aged_brie(self, item):
        item.sell_in -= 1
        item.quality += 1 if item.sell_in >= 0 else 2

    def update_backstage_pass(self, item):
        item.sell_in -= 1
        if item.sell_in >= 10:
            item.quality += 1
        elif 5 <= item.sell_in < 10:
            item.quality += 2
        elif item.sell_in >= 0:
            item.quality += 3

    def update_normal_item(self, item):
        item.sell_in -= 1
        if item.sell_in > 0:
            item.quality -= 1
        else:
            item.quality -= 2

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return f"{self.name}, {self.sell_in}, {self.quality}"
