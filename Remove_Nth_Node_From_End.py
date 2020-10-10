# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
#         current = ListNode(0)
#         current.next = head
#         first = current
#         second = current
#         currLen = 1
#         while first.next != None:
#             currLen += 1
#             first = first.next
            
#         toRemove = currLen - (n + 1)
#         for i in range(toRemove):
#             second = second.next
            
#         second.next = second.next.next
#         return current.next
        
        
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        for x in range(0,n+1):
            first = first.next
        while first != None:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next
