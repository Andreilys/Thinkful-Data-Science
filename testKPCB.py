import unittest
from KPCB import hashMap

class hashMapTests(unittest.TestCase):
    def test(self):
        self.assertEqual(fun(3),4)

def main():
    newHash = hashMap(9)
    print(newHash.data)

if __name__ == "__main__":
    main()
