"""
Sort a linked list in O(n log n) time using constant space complexity.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def get_middle(A):
    mid = end = A
    while end.next and end.next.next:
        mid = mid.next
        end = end.next.next
    return mid


def merge_lists(A, B):
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


# @param A : head node of linked list
# @return the head node in the linked list
def sortList(A):
    if not A or not A.next:
        return A
    middle = get_middle(A)
    second_half = middle.next
    middle.next = None
    left = sortList(A)
    right = sortList(second_half)
    sorted_list = merge_lists(left, right)
    return sorted_list
