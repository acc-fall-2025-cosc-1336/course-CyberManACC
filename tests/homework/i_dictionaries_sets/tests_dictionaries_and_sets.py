import os, sys
_here = os.path.abspath(os.path.dirname(__file__))
_root = os.path.abspath(os.path.join(_here, "..", "..", ".."))
if _root not in sys.path:
    sys.path.insert(0, _root)

import unittest
from src.homework.i_dictionaries_sets.dictionary import (
    add_inventory,
    remove_inventory_widget,
)

class Test_Config(unittest.TestCase):
    def test_add_inventory(self):
        inventory = {}
        # add new
        add_inventory(inventory, "Widget1", 10)
        self.assertIn("Widget1", inventory)
        self.assertEqual(inventory["Widget1"], 10)

        # update existing (add)
        add_inventory(inventory, "Widget1", 25)
        self.assertEqual(inventory["Widget1"], 35)

        # update existing (subtract)
        add_inventory(inventory, "Widget1", -10)
        self.assertEqual(inventory["Widget1"], 25)

    def test_remove_inventory_widget(self):
        inventory = {}
        add_inventory(inventory, "widget1", 5)
        add_inventory(inventory, "widget2", 12)

        msg = remove_inventory_widget(inventory, "widget1")
        self.assertEqual(msg, "Record deleted")
        self.assertEqual(len(inventory), 1)
        self.assertIn("widget2", inventory)

        # removing missing should say not found
        msg2 = remove_inventory_widget(inventory, "widget1")
        self.assertEqual(msg2, "Item not found")


if __name__ == "__main__":
    unittest.main(verbosity=2)
