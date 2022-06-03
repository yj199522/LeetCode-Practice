# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        d=ListNode()
        new=d
        carry=0
        while l1 or l2:
            if l1 is None and l2 is not None:
                rawNum = l2.val
                l2 = l2.next
            elif l2 is None and l1 is not None:
                rawNum = l1.val
                l1 = l1.next
            else:
                rawNum=l1.val + l2.val
                l1 = l1.next
                l2 = l2.next
            
            digit = carry + rawNum
            new.next = ListNode(digit % 10)
            new=new.next
            carry = digit // 10
        
        if carry:
            new.next = ListNode(1)
        
        return d.next