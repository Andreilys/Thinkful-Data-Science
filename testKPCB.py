import unittest
from KPCB import hashMap


class hashMapTests(unittest.TestCase):
    def setUp(self):
        newHash = hashMap(8)
        newHash.set("Blueberries", 5)
        newHash.set("Apples", 9)
        newHash.set("Lemons", 10)
        return newHash

    def testCreatingHashMap(self):
        newHash = self.setUp()
        self.assertEqual(len(newHash.data), 8)

    def testSettingValue(self):
        newHash = hashMap(2)
        newHash.set("Blueberries", 5)
        self.assertEqual(newHash.set("Lemons", 10), True)
        # Testing whether setting after the hashMap is full returns False
        self.assertEqual(newHash.set("Melons", 10), False)
        self.assertEqual(newHash.itemCount, 2)
        self.assertEqual(newHash.get("Blueberries"), 5)

    def testGettingValue(self):
        newHash = self.setUp()
        self.assertEqual(newHash.get("Blueberries"), 5)
        # Testing a false input
        self.assertEqual(newHash.get("Melons"), None)

    def testDeletingValue(self):
        newHash = self.setUp()
        self.assertEqual(newHash.delete("Blueberries"), 5)
        # Testing a false input
        self.assertEqual(newHash.get("Melons"), None)

    def testLoadMethod(self):
        newHash = self.setUp()
        self.assertEqual(newHash.load(), float(3)/8)

def main():
    unittest.main()


if __name__ == '__main__':
    main()
