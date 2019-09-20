#Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

#Example:

#Input:
#[
#  1->4->5,
#  1->3->4,
#  2->6
#]

#Output: 1->1->2->3->4->4->5->6


from Queue import PriorityQueue
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = point = ListNode(0)
        q = PriorityQueue()
        for l in lists:
            print(l)
            if l:
                q.put((l.val, l))
        while not q.empty():
            val, node = q.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                q.put((node.val, node))
        return head.next
