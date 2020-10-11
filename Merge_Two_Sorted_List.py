# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, a, b):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s = ListNode(None)
        if not a:
            return b
        if not b:
            return a
        if a and b:
            if a.val <= b.val:
                s = a
                a = s.next
            else:
                s = b
                b = s.next
        newHead = s
        while a and b:
            if a.val <= b.val:
                s.next = a
                s = a
                a = s.next
            else:
                s.next = b
                s = b
                b = s.next
        if not a:
            s.next = b
        if not b:
            s.next = a
        return newHead
