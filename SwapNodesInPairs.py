# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        p = head
        new_head = p.next
        while 1:
            q = p.next
            temp = q.next
            q.next = p
            if temp == None or temp.next == None:
                p.next = temp
                break
            p.next = temp.next
            p = temp
        return new_head
            
