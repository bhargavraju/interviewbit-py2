"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# @param A : head node of linked list
# @param B : integer
# @return the head node in the linked list
def partition(self, A, B):
    dummy1, dummy2 = ListNode('dummy1'), ListNode('dummy2')
    tail1, tail2 = dummy1, dummy2
    while A is not None:
        if A.val < B:
            tail1.next = A
            tail1 = A
        else:
            tail2.next = A
            tail2 = A
        A = A.next
    tail1.next = dummy2.next
    tail2.next = None
    return dummy1.next
