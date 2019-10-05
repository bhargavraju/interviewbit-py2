"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# @param A : head node of linked list
# @return the head node in the linked list
def deleteDuplicates(A):
    dummy = ListNode(0)
    dummy.next = A
    tail = dummy
    while A:
        curr = A
        while A.next and A.next.val == curr.val:
            A = A.next
        if curr == A:
            tail = tail.next
        else:
            tail.next = A.next
        A = A.next
    return dummy.next
