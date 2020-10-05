class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # TC: O(n), SC: O(n)
        mapping = {}
        for i in range(len(nums)):
            pair = target - nums[i]
            if pair not in mapping:
                mapping[nums[i]] = i
            else:
                return [mapping[pair], i]
        
