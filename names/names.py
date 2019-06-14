import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value and self.left:
            self.left.insert(value)
        elif value < self.value:
            self.left = BinarySearchTree(value)
        elif value > self.value and self.right:
            self.right.insert(value)
        elif value > self.value:
            self.right = BinarySearchTree(value)

    def contains(self, target):
        current = self
        answer = False

        while True:
            if current.value == target:
                answer = True
                break
            elif current.value > target:
                if current.left != None:
                    current = current.left
                else:
                    break
            elif current.value < target:
                if current.right != None:
                    current = current.right
                else:
                    break
        return answer

    def get_max(self):
        if self.right == None:
            return self.value
        return self.right.get_max()


    def for_each(self, cb):
        current = self
        if current.left != None:
            current.left.for_each(cb)
        if current.right != None:
            current.right.for_each(cb)
        return cb(current.value)

sorted_binary = BinarySearchTree(names_1[0])


duplicates = []
for x in range(1, len(names_1)):
    sorted_binary.insert(names_1[x])

for i in range(0, len(names_2)):
    if sorted_binary.contains(names_2[i]):
        duplicates.append(names_2[i])

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

