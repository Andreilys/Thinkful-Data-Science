"""
Andrei Lyskov
www.andreilyskov.com
www.linkedin.com/in/andreilyskov

This program implements a fixed-size hash map that associates string keys with arbitrary data object references
"""


# hashMap class utilizes the methods: constructor (creates the fixed size hash map)
# set (set a key and value pair), get (retrieve the associated value from the key)
# delete (delete the key and value pair based on the key) and load (return a float
# which shows the number of items in the hashmap divided by the size of the hashmap
class hashMap:
    # Initialize the class
    def __init__(self, size):
        self.data = []
        self.itemCount = 0
        self.size = size
        if (size <= 0):
            return 0
        else:
            for i in range(size):
                self.data = [None] * size

    def hashFunction(self, key):
        return hash(key) % self.size

    # The set method takes a key and value pair, with the key being hashed
    # before being stored in the data array.
    def set(self, key, value):
        hashedValue = self.hashFunction(key)
        if self.data[hashedValue] == None:
            self.data[hashedValue] = [(key, value)]
            self.itemCount = self.itemCount + 1
            return True
        else:
            # We're checking first to see if the hashMap is already full or not
            # seeing as load cannot exceed 1
            if (float(self.itemCount + 1))/self.size <= 1:
                self.data[hashedValue].append((key, value))
                self.itemCount = self.itemCount + 1
                return True
            else:
                return False

    # The get method takes in a key, retrieves the hash value, and traverses the
    # stored list if there are additional values that hash to the same index
    def get(self, key):
        hashedValue = self.hashFunction(key)
        if self.data[hashedValue]:
            lengthOfBucket = len(self.data[hashedValue])
            for i in range(lengthOfBucket):
                keyValue = self.data[hashedValue][i][0]
                if keyValue == key:
                    return self.data[hashedValue][i][1]
        else:
            return None

    # The delete method takes in a key
    def delete(self, key):
        hashedValue = self.hashFunction(key)
        if self.data[hashedValue]:
            lengthOfBucket = len(self.data[hashedValue])
            for i in range(lengthOfBucket):
                keyValue = self.data[hashedValue][i][0]
                if keyValue == key:
                    deletedValue = keyValue
                    self.data[hashedValue].pop(i)
                    # Check to see if there are any elements left in the list.
                    # If not, set list to 0
                    if not self.data[hashedValue]:
                        self.data[hashedValue] = None
                    self.itemCount = self.itemCount - 1
                    return deletedValue
        else:
            return None

    # The load method returns the number of items in the array, divided by the size
    # of the array
    def load(self):
        return float(self.itemCount) / self.size


def main():
    newHash = hashMap(9)
    newHash.set("Blueberries", 5)
    newHash.set("Apples", 9)
    newHash.set("Lemons", 10)
    print(newHash.get("Apples"))
    print(newHash.delete("Blueberries"))
    print(newHash.set("Blueberries", 50))
    # print(newHash.delete("Lemons"))
    # print(newHash.delete("Blueberries"))
    print(newHash.data)
    print(newHash.load())

if __name__ == "__main__":
    main()
