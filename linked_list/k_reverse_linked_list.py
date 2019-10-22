"""
Given a singly linked list and an integer K, reverses the nodes of the

list K at a time and returns modified linked list.

The length of the list is divisible by K

Given linked list 1 -> 2 -> 3 -> 4 -> 5 -> 6 and K=2,

You should return 2 -> 1 -> 4 -> 3 -> 6 -> 5

Try to solve the problem using constant extra space.

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
    return curr


# @param A : head node of linked list
# @param B : integer
# @return the head node in the linked list
def reverseList(A, B):
    if B < 2:
        return A
    dummy = ListNode('dummy')
    dummy.next = A
    prev, behind = dummy, A
    while behind:
        ahead = behind
        for i in range(B-1):
            ahead = ahead.next
        end = reverse_list(behind, ahead)
        prev.next = ahead
        behind.next = end
        prev = behind
        behind = behind.next
    return dummy.next
