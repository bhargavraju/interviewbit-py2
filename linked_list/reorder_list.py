"""
Given a singly linked list
L : L0 -> L1 -> L2 -> ...... -> Ln-1 -> Ln

reorder it to
L : L0 -> Ln -> L1 -> Ln-1 -> ......

You must do this without altering the node values and in-place
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def reverse_list(start, end):
    prev, curr = None, start
    while prev is not end:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next


# @param A : head node of linked list
# @return the head node in the linked list
def reorderList(A):
    head = mid = tail = A
    while tail.next and tail.next.next:
        mid = mid.next
        tail = tail.next.next
    if tail.next:
        tail = tail.next
        reverse_list(mid.next, tail)
    else:
        reverse_list(mid, tail)
    while head.next is not tail and head is not tail:
        left_next = head.next
        head.next = tail
        right_next = tail.next
        tail.next = left_next
        head = left_next
        tail = right_next
    return A
