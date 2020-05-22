# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        while head:
            temp = head
            head = head.next
            temp.next = prev
            prev = temp
        return prev
        # if head == None or head.next == None:
        #     return head
        # p = self.reverseList(head.next)
        # head.next.next = head
        # head.next = None
        # return p
        # prev = None
        # curr = head
        # while curr != None:
        #     nextTemp = curr.next
        #     # print("Temp: ", nextTemp)
        #     curr.next = prev
        #     # print("Next Curr: ", curr.next)
        #     prev = curr
        #     # print("Prev: ", prev)
        #     curr = nextTemp
        #     # break
        # return prev
