class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        init = 0
        for i in range(len(nums)):
            if nums[i] != init:
                return init
            init += 1
        
        return len(nums)
