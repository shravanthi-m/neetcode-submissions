# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        len = 0
        curr = head
        while curr != None:
            len += 1
            curr = curr.next
        print(len)
        ind = len - n

        if ind == 0:
            return head.next
        l = 0
        curr = head
        while l != len-n:
            l += 1
            prev = curr
            curr = curr.next
        prev.next = curr.next       
        return head