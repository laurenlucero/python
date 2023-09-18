# -*- coding: utf-8 -*-
import unittest
from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_update_quality_normal_item(self):
        # Create an item with positive quality and sell-in
        items = [Item("Normal", 5, 10), Item("NormalMinQuality", 5, 0)]
        gilded_rose = GildedRose(items)

        # Call the update_quality method to simulate the current behavior
        gilded_rose.update_quality()

        # Verify that the item's state matches the current behavior (decrement by 1)
        self.assertEqual(items[0].name, "Normal")
        self.assertEqual(items[0].sell_in, 4)
        self.assertEqual(items[0].quality, 9)

        self.assertEqual(items[1].name, "NormalMinQuality")
        self.assertEqual(items[1].sell_in, 4)
        self.assertEqual(items[1].quality, 0)

    def test_update_quality_never_negative(self):
        item = [Item("Never Negative", -1, 0)]
        gilded_rose = GildedRose(item)

        gilded_rose.update_quality()

        self.assertEqual(item[0].name, "Never Negative")
        self.assertEqual(item[0].sell_in, -2)
        self.assertEqual(item[0].quality, 0)

    def test_update_quality_aged_brie(self):
        items = [Item("Aged Brie", 5, 10), Item("Aged Brie", -1, 10), Item("Aged Brie", -10, 49)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(items[0].name, "Aged Brie")
        self.assertEqual(items[0].sell_in, 4)
        self.assertEqual(items[0].quality, 11)
        # negative sell-in should increment quality of aged brie by 2
        self.assertEqual(items[1].sell_in, -2)
        self.assertEqual(items[1].quality, 12)
        # quality does not exceed 50
        self.assertEqual(items[2].sell_in, -11)
        self.assertEqual(items[2].quality, 50)

    def test_update_quality_backstage_passes(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 11, 0), Item("Backstage passes to a TAFKAL80ETC concert", 9, 0), Item("Backstage passes to a TAFKAL80ETC concert", 4, 0), Item("Backstage passes to a TAFKAL80ETC concert", -1, 0), Item("Backstage passes to a TAFKAL80ETC concert", 11, 50)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(items[0].name, "Backstage passes to a TAFKAL80ETC concert")
        # quality increases by 1 when sell-in > 10
        self.assertEqual(items[0].sell_in, 10)
        self.assertEqual(items[0].quality, 1)
        # quality increases by 2 when sell-in 6-10
        self.assertEqual(items[1].sell_in, 8)
        self.assertEqual(items[1].quality, 2)
        # quality increases by 3 when sell-in <= 5
        self.assertEqual(items[2].sell_in, 3)
        self.assertEqual(items[2].quality, 3)
        # quality is 0 when sell-in is negative (expired)
        self.assertEqual(items[3].sell_in, -2)
        self.assertEqual(items[3].quality, 0)
        # quality does not exceed 50
        self.assertEqual(items[4].sell_in, 10)
        self.assertEqual(items[4].quality, 50)

    def test_update_quality_sulfuras(self):
        item = [Item("Sulfuras, Hand of Ragnaros", 5, 10)]
        gilded_rose = GildedRose(item)

        gilded_rose.update_quality()
        # Legendary item, no change needed
        self.assertEqual(item[0].name, "Sulfuras, Hand of Ragnaros")
        self.assertEqual(item[0].sell_in, 5)
        self.assertEqual(item[0].quality, 10)

    def test_update_quality_never_exceeds_50(self):
        item = [Item("NoMoreThan50", 5, 51)]
        gilded_rose = GildedRose(item)

        gilded_rose.update_quality()

    # TODO quality should not exceed 50
        self.assertEqual(item[0].name, "NoMoreThan50")
        self.assertEqual(item[0].sell_in, 4)
        self.assertEqual(item[0].quality, 50)

    def test_update_quality_normal_expired_items(self):
        # Create an item negative sell-in (expired)
        items = [Item("NormalExpired", -1, 10), Item("BeyondExpired", -10, 0)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        # quality decrements by 2
        self.assertEqual(items[0].name, "NormalExpired")
        self.assertEqual(items[0].sell_in, -2)
        self.assertEqual(items[0].quality, 8)
        # quality stays at 0
        self.assertEqual(items[1].name, "BeyondExpired")
        self.assertEqual(items[1].sell_in, -11)
        self.assertEqual(items[1].quality, 0)

    def test_update_quality_extreme_sell_in(self):
        # Create an item negative sell-in (expired)
        items = [Item("Positive", 1000, 10), Item("Negative", -1000, 0)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        # quality decrements by 2
        self.assertEqual(items[0].name, "Positive")
        self.assertEqual(items[0].sell_in, 999)
        self.assertEqual(items[0].quality, 9)
        # quality stays at 0
        self.assertEqual(items[1].name, "Negative")
        self.assertEqual(items[1].sell_in, -1001)
        self.assertEqual(items[1].quality, 0)

if __name__ == "__main__":
    unittest.main()
