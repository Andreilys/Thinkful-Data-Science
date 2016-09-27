"""
Andrei Lyskov
www.andreilyskov.com
www.linkedin.com/in/andreilyskov

This program implements a fixed-size hash map that associates string keys with arbitrary data object references
"""


# hashMap class utilizes the constructor, set, get, delete and load functions
class hashMap:
    # Initialize the function
    def __init__(self):
        self.data = []
        self.itemCount = 0
        self.size = 0

    # constructor is a method which initializes the fixed map, assuming it is provided
    # an appropriate int size variable. It returns the hashMap instance upon completion.
    def constructor(self, size):
        self.size = size
        if (size <= 0):
            return 0
        else:
            for i in range(size):
                self.data.append([])
        return self

    # Set method stores a key and value within a list of lists as long as there is
    # still an empty list to store the data in. It returns true or false depending on its success.
    def set(self, key, value):
        for i in range(len(self.data)):
            if not self.data[i]:
                self.data[i].append(key)
                self.data[i].append(value)
                self.itemCount = self.itemCount + 1
                return True
        return False

    # The get method goes through the data structure to find the appropriate key, returning
    # None or the value if its found.
    def get(self, key):
        for i in range(len(self.data)):
            if self.data[i]:
                if key == self.data[i][0]:
                    return self.data[i][1]
        return None

    # The delete method takes in a key, and deletes it from the list of lists.
    # It returns None or the value its deleted.
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

    # The load method returns the number of items in the array, divided by the size
    # of the array
    def load(self):
        return float(self.itemCount) / self.size


def tests(newHash):
    print(newHash.constructor(3))
    print(newHash.data)
    # Filling the hashmap to its full capacity and checking to see that it works
    newHash.set("Apples", 9)
    newHash.set("Oranges", 7)
    newHash.set("Lemons", 3)
    print(newHash.data)
    print(newHash.load())
    print(newHash.get("Apples"))
    print(newHash.get("Oranges"))
    newHash.delete("Apples")
    newHash.delete("Lemons")
    print(newHash.data)
    print(newHash.load())
    # Testing the return on invalid input
    print(newHash.get("Blueberries"))
    print(newHash.delete("Cranberries"))
    print(newHash.set("Watermelons", 8))
    print(newHash.set("Mangos", 3))
    print(newHash.set("Grapes", 3))


def main():
    newHash = hashMap()
    tests(newHash)

if __name__ == "__main__":
    main()
