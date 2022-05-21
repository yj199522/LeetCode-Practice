# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        
        if list1 is None:
            return list2
        
        if list2 is None:
            return list1
    
        result = ListNode()
        prevList = result
        
        while list1 and list2:
            print(list1)
            if list1.val <= list2.val:
                prevList.next = list1
                list1 = list1.next
            else:
                prevList.next = list2
                list2 = list2.next
            prevList = prevList.next
        if list1:
            prevList.next = list1
        
        if list2:
            prevList.next = list2
        
        return result.next
#         data = []
#         while list1 is not None:
#             data.append(list1.val)
#             list1 = list1.next
#         while list2 is not None:
#             data.append(list2.val)
#             list2 = list2.next
#         data = sorted(data)
#         result = ListNode(data[0])
#         dummy = result
#         for i in range(1,len(data)):
#             node = ListNode(data[i])
#             dummy.next = node
#             dummy = dummy.next
#         return result
            