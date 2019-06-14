Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?
- O(1) The code and runtime will remain the same no matter how many times you run it.

2. What is the space complexity of your ring buffer's `append` function?
- The space complexity will be constant.

3. What is the runtime complexity of your ring buffer's `get` method?
- O(n) I made a list comprehension that will loop through self.storage and inside the loop, an if-statement is created and it checks to see if i is not equal to None, so we can output the ring buffer in order.

4. What is the space complexity of your ring buffer's `get` method?
- I would say O(1) because everything is stored into one space, which is the list comprehension I created.

5. What is the runtime complexity of the provided code in `names.py`?
- O(n) I could've gone with O(n^2) because we have two for loops but they are not nested together so it will loop through separately. One for loop is going to loop through each name and insert it whereas the second for loop will check to see if names have been contain, it will be pushed to the duplicates list.

6. What is the space complexity of the provided code in `names.py`?
- O(n) n represents the size of the list that contains all of the matched names.

7. What is the runtime complexity of your optimized code in `names.py`?
- O(n log n) We are using contains from the BinarySearchTree class and is checking to see if the list contains the item from name 2.

8. What is the space complexity of your optimized code in `names.py`?
- O(n) The N comes from the binary search tree and the second comes from the length of the duplicates list.
