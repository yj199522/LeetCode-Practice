# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        data = []
        if head is None:
            return []
        while head is not None:
            data.append(head.val)
            head = head.next
        data.pop(len(data)-n)
        
        if len(data) == 0:
            return None
        result = ListNode(data[0])
        dummy = result
        for i in range(1,len(data)):
            node = ListNode(data[i])
            dummy.next = node
            dummy = dummy.next
        return result
        