#Given nums = [1,1,2],

#Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

#It doesn't matter what you leave beyond the returned length.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        if len(nums) ==0:
            return 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j += 1
        return j
