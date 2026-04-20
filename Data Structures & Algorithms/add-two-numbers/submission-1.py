# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if (l1 is None) and (l2 is None):
            return None
        if l1 is None:
            return l2
        if l2 is None:
            return l2
        carry = 0
        curr1 = l1
        curr2 = l2
        dummy = ListNode(-1)
        curr = dummy
        while curr1 and curr2:
            s = curr1.val + curr2.val + carry
            carry = s//10
            s = s%10
            curr.next = ListNode(s)
            curr = curr.next
            curr1 = curr1.next
            curr2 = curr2.next
        
        while curr1:
            s = curr1.val + carry
            carry = s//10
            s = s%10
            curr.next = ListNode(s)
            curr = curr.next
            curr1 = curr1.next
        while curr2:
            s = curr2.val + carry
            carry = s//10
            s = s%10
            curr.next = ListNode(s)
            curr = curr.next
            curr2 = curr2.next

        if carry>0:
            curr.next = ListNode(carry)

        return dummy.next

