Add your answers to the questions below.

1. What is the runtime complexity of your `depth_first_for_each` method?

O(n) because we are traversing each node only once and popping it off the 
stack once it has been visited. 

2. What is the space complexity of your `depth_first_for_each` function?

O(n) because we use a stack that accumulates to N input.

3. What is the runtime complexity of your `breadth_first_for_each` method?

4. What is the space complexity of your `breadth_first_for_each` method?


5. What is the runtime complexity of the provided code in `names.py`?

O(n^2) because it uses a nested for loop of both arrays comparing each element
individually to every element of the other array and incrementing the index and doing it all over again.

6. What is the space complexity of the provided code in `names.py`?

O(1) because space isn't being allocated that equates a worst case of N input.

7. What is the runtime complexity of your optimized code in `names.py`?

O(n) because I search through the list in one
pass of N input.

8. What is the space complexity of your optimized code in `names.py`?

O(n) because I used a dictionary to keep track of whether I've seen the element before in the other file or not.
This is assuming one of the given array is considered n input size. 

