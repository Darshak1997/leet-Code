import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        temp = heapq.nlargest(k, nums)
        return(temp[k-1])
