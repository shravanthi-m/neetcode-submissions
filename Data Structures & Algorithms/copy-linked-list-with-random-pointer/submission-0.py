"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodesCopy = {None: None}

        curr = head
        while curr:
            copy = Node(curr.val)
            nodesCopy[curr] = copy
            curr = curr.next
        curr = head
        while curr:
            copy = nodesCopy[curr]
            copy.next = nodesCopy[curr.next]
            copy.random = nodesCopy[curr.random]
            curr = curr.next
        return nodesCopy[head]