"""
Reverse a linked list. Do it in-place and in one-pass.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# @param A : head node of linked list
# @return the head node in the linked list
def reverseList(A):
    prev, curr = None, A
    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev