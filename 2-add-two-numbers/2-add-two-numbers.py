# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1= ''
        list2 = ''
        while l1 is not None:
            list1+=str(l1.val)
            l1 = l1.next
        while l2 is not None:
            list2+=str(l2.val)
            l2 = l2.next
        
        total = str(int(list1[::-1]) + int(list2[::-1]))[::-1]
        result = ListNode(total[0])
        data = result
        for i in range(1,len(total)):
            node = ListNode(total[i])
            data.next = node
            data = data.next
        return result