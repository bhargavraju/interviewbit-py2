"""
Given a read only array of n + 1 integers between 1 and n, find one number that repeats in linear time using
less than O(n) space and traversing the stream sequentially O(1) times.

Sample Input:
[3 4 1 4 1]
Sample Output:
1

If there are multiple possible answers ( like in the sample case above ), output any one.
If there is no duplicate, output -1
"""


# @param A : tuple of integers
# @return an integer
def repeatedNumber(A):
    n = len(A) - 1
    if n <= 0:
        return -1
    slow = A[0]
    fast = A[A[0]]

    while fast != slow:
        slow = A[slow]
        fast = A[A[fast]]

    slow = 0
    while slow != fast:
        slow = A[slow]
        fast = A[fast]

    return slow


"""
Explanation:

If there is no duplicate in the array, we can map each indexes to each numbers in this array. In other words, we can 
have a mapping function f(index) = number. For example, let's assume nums = [2,1,3], then the mapping function is 
0->2, 1->1, 2->3.

If we start from index = 0, we can get a value according to this mapping function, and then we use this value as a 
new index and, again, we can get the other new value according to this new index. We repeat this process until the 
index exceeds the array. Actually, by doing so, we can get a sequence. Using the above example again, the sequence 
we get is 0->2->3. (Because index=3 exceeds the array's size, the sequence terminates!)

However, if there is duplicate in the array, the mapping function is many-to-one.
For example, let's assume
nums = [2,1,3,1], then the mapping function is 0->2, {1,3}->1, 2->3. Then the sequence we get definitely has a cycle.
 0->2->3->1->1->1->1->1->........ The starting point of this cycle is the duplicate number.
We can use Floyd's Tortoise and Hare Algorithm to find the starting point.

Try this out with other examples on paper to get a better understanding.
"""
