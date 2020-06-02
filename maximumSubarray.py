class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            # print(nums[i-1])
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
                # print(nums)
        return max(nums)
#         maxSum = float("-inf")
#         rightPointer = len(nums)-1
#         leftPointer = 0
#         if len(nums) == 0:
#             return 0
#         if len(nums) == 1:
#             return nums[0]
        
#         def recurr(nums, leftPointer, rightPointer, maxSum):
#             while rightPointer >=  leftPointer:
#                 currSum = sum(nums[leftPointer:rightPointer+1])
#                 maxSum = max(maxSum, currSum)
#                 rightPointer -= 1
#             if leftPointer == len(nums)-1:
#                 return maxSum
#             else:
#                 return recurr(nums[leftPointer+1:], 0, len(nums[1:]), maxSum)
            
#         return recurr(nums, leftPointer, rightPointer, maxSum)
        
        
