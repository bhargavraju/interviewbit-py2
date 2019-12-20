"""
A linked list is given such that each node contains an additional random pointer which could point to any node
in the list or NULL. Return a deep copy of the list.

Example
Given list
   1 -> 2 -> 3
with random pointers going from
  1 -> 3
  2 -> 1
  3 -> 1
You should return a deep copy of the list. The returned answer should not contain the same node as the original list,
but a copy of them. The pointers in the returned list should not link to any node in the original input list.
"""


class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


# @param head, a RandomListNode
# @return a RandomListNode
def copyRandomList(head):
    parser = head
    dummy = copy_parser = RandomListNode(0)
    node_map = {}
    while parser:
        copy_node = RandomListNode(parser.label)
        copy_parser.next = copy_node
        node_map[parser] = copy_node
        parser = parser.next
        copy_parser = copy_parser.next
    copy_parser.next = None
    random_parser = dummy.next
    while random_parser:
        random_parser.random = node_map[head.random] if head.random else None
        head = head.next
        random_parser = random_parser.next
    return dummy.next
