# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        if head.next is None:
            return head
        
        result = ListNode()
        prevList = result
        while head:
            if head.next is not None:
                prevList.next = head.next
                head.next = head.next.next
                prevList = prevList.next
            if prevList is not None:
                prevList.next = head
                prevList = prevList.next
            head = head.next
        return result.next
        