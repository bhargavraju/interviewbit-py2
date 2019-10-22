"""
Sort a linked list using insertion sort.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# @param A : head node of linked list
# @return the head node in the linked list
def insertionSortList(A):
    if not A or not A.next:
        return A
    head = A
    A = A.next
    while A:
        point = head
        while point != A:
            if point.val > A.val:
                tmp = A.val
                A.val = point.val
                point.val = tmp
            else:
                point = point.next
        A = A.next

    return head
