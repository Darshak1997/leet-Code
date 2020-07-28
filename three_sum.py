class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i-1] != nums[i]:
                self.twoSum(nums, i, res)
        return res
    
    def twoSum(self, nums, i, res):
        lo, hi = i+1, len(nums)-1
        while lo < hi:
            currSum = nums[i] + nums[lo] + nums[hi]
            if currSum < 0 or (lo > i+1 and nums[lo] == nums[lo-1]):
                lo += 1
            elif currSum > 0 or (hi < len(nums)-1 and nums[hi] == nums[hi+1]):
                hi -= 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                
