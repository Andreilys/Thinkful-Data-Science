"""
Time Complexities:
Using only primitive types, implement a fixed-size hash map
that associates string keys with arbitrary data object references
"""


class hashMap:
    def __init__(self):
        self.data = []
        self.itemCount = 0
        self.size = 0

    def constructor(self, size):
        self.size = size
        if (size < 0):
            return 0
        else:
            for i in range(size):
                self.data.append([])
            return self.data

    def set(self, key, value):
        for i in range(len(self.data)):
            if not self.data[i]:
                self.data[i].append(key)
                self.data[i].append(value)
                self.itemCount = self.itemCount + 1
                return True
        return False

    def get(self, key):
        for i in range(len(self.data)):
            if self.data[i]:
                if key == self.data[i][0]:
                    return self.data[i][1]
        return None

    def delete(self, key):
        for i in range(len(self.data)):
            if self.data[i]:
                if key == self.data[i][0]:
                    value = self.data[i][1]
                    self.data[i].remove(value)
                    self.data[i].remove(key)
                    self.itemCount = self.itemCount - 1
                    return value
        return None

    def load(self):
        return float(self.itemCount)/self.size


def tests(newHash):
    newHash.constructor(3)
    newHash.set("hey", 9)
    newHash.set("nope", 7)
    newHash.set("ok", 3)
    print(newHash.data)
    newHash.delete("hey")
    print(newHash.get("nope"))
    newHash.set("nahh", 5)
    print(newHash.data)
    print(newHash.load())
    print(newHash.delete("nope"))

def main():
    newHash = hashMap()
    tests(newHash)

if __name__ == "__main__":
    main()
