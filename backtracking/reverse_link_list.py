"""
Reverse a linked list using recursion.

Example :
Given 1->2->3->4->5->NULL,
return 5->4->3->2->1->NULL.
"""


# @param A : head node of linked list
# @return the head node in the linked list
def reverseList(A):
    if not A or not A.next:
        return A
    p = reverseList(A.next)
    A.next.next = A
    A.next = None
    return p
