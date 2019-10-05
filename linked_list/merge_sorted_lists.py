"""
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists, and should also be sorted.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# @param A : head node of linked list
# @param B : head node of linked list
# @return the head node in the linked list
def mergeTwoLists(A, B):
    dummy = ListNode('dummy')
    curr = dummy
    while A and B:
        if A.val <= B.val:
            curr.next = A
            A = A.next
        else:
            curr.next = B
            B = B.next
        curr = curr.next
    if A:
        curr.next = A
    else:
        curr.next = B
    return dummy.next
