# Input: [1,2,3,1]
# Output: true

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for i in nums:
            hashset.add(i)
        if len(nums) != len(hashset):
            return True
        else:
            return False
