# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None
        
        ptr1 = headA
        ptr2 = headB
        
        while ptr1 != ptr2:
            ptr1 = headB if ptr1 == None else ptr1.next
            ptr2 = headA if ptr2 == None else ptr2.next
            
        return ptr1
