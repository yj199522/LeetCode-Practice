# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def Sorting(arr, start=0, end=None):
    if end == None:
        nums = len(arr)
        end = nums - 1
    if start < end:
        pivot = partition(arr, start, end)
        Sorting(arr, start, pivot-1)
        Sorting(arr, pivot+1, end)
    return arr

def partition(arr, start=0, end=None):
    if end == None:
        end = len(arr) - 1
    l,r = start, end-1
    while(l<r):
        if arr[l]<= arr[end]:
            l+=1
        elif arr[r] > arr[end]:
            r-=1
        else:
            arr[l], arr[r] = arr[r], arr[l]
    if arr[l] > arr[end]:
        arr[l], arr[end] = arr[end], arr[l]
        return l
    else:
        return end
    
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==0:
            return None
        arr = []
        idx = 0
        while idx < len(lists):
            head = lists[idx]
            while head:
                arr.append(head.val)
                head=head.next
            idx+=1
        arr = Sorting(arr)
        if len(arr)==0:
            return None
        head = ListNode(arr[0])
        l = head
        for i in range(1, len(arr)):
            l.next = ListNode(arr[i])
            l = l.next
        return head
            
            