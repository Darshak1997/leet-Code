class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = collections.Counter(nums)
        return max(n.keys(), key=n.get)
