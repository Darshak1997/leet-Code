class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastIndex = len(nums)-1
        currIndex = 0
        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= lastIndex:
                lastIndex = i
        return lastIndex == 0
            
