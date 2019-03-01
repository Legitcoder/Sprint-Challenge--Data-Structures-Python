Add your answers to the questions below.

1. What is the runtime complexity of your `depth_first_for_each` method?

2. What is the space complexity of your `depth_first_for_each` function?

3. What is the runtime complexity of your `breadth_first_for_each` method?

4. What is the space complexity of your `breadth_first_for_each` method?


5. What is the runtime complexity of the provided code in `names.py`?

O(n^2) because it uses a nested for loop of both arrays comparing each element n times
while iterating through the same

6. What is the space complexity of the provided code in `names.py`?

O(1) because space isn't being allocated that equates a worst case of N input.

7. What is the runtime complexity of your optimized code in `names.py`?

O(n+k) because I use extends to merge the arrays and search through the list in one
pass of N input.

8. What is the space complexity of your optimized code in `names.py`?

O(n) because I used a dictionary to keep track of whether I've seen the element before or not and
this grows to N input.
