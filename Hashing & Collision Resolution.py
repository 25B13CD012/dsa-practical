class ChainHash:

    def __init__(self, m):
        self.table = [[] for _ in range(m)]

    def put(self, x):
        b = self.table[x % len(self.table)]

        if x not in b:
            b.append(x)

    def has(self, x):
        return x in self.table[x % len(self.table)]

    def erase(self, x):
        b = self.table[x % len(self.table)]

        if x not in b:
            return False

        b.remove(x)
        return True

    def show(self):
        for i, b in enumerate(self.table):
            print(f"{i}:", *b)


# Create hash table
h = ChainHash(5)

# Insert values
for x in (10, 15, 20, 7):
    h.put(x)

# Display table
h.show()

# Search
print("Find 15:", h.has(15))

# Delete
print("Remove 15:", h.erase(15))

# Search again
print("Find 15:", h.has(15))