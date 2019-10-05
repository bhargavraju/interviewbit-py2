"""
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:

Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# @param A : head node of linked list
# @param B : integer
# @return the head node in the linked list
def rotateRight(A, B):
    behind = ahead = A
    for i in range(B):
        ahead = ahead.next
        if ahead is None:
            ahead = A
    if behind is ahead:
        return A
    else:
        while ahead.next:
            behind = behind.next
            ahead = ahead.next
        head = behind.next
        behind.next = None
        ahead.next = A
        return head
