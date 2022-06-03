# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result=ListNode()
        dummy=result
        carry=0
        while l1 or l2:
            if l1 is None and l2 is not None:
                value = l2.val
                l2 = l2.next
            elif l2 is None and l1 is not None:
                value = l1.val
                l1 = l1.next
            else:
                value=l1.val + l2.val
                l1 = l1.next
                l2 = l2.next
            
            digit = carry + value
            dummy.next = ListNode(digit % 10)
            dummy=dummy.next
            carry = digit // 10
        
        if carry:
            dummy.next = ListNode(1)
        
        return result.next