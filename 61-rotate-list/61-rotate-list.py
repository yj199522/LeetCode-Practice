# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        if k is 0:
            return head
        result = []
        while head:
            result.append(head.val)
            head = head.next
        if k > len(result):
            k = k%len(result)
        for i in range(k):
            result = [result[-1]] + result[:-1]
        
        data = ListNode()
        dummy = data
        
        for i in result:
            node = ListNode(i)
            dummy.next = node
            dummy = dummy.next
        
        return data.next
        
        