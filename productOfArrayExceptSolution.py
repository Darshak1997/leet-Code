class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        L = [1]*n
        R = [1]*n
        res = [1]*n
        for i in range(1, n):
            L[i] = L[i-1]*nums[i-1]
        for i in reversed(range(n-1)):
            R[i] = R[i+1]*nums[i+1]
        for i in range(n):
            res[i] = L[i]*R[i]
        return res
        
        
        # res = [1]*len(nums)
        # num = 0
        # while num < len(nums):
        #     for i in range(len(nums)):
        #         if i == num:
        #             continue
        #         else:
        #             res[num] *= nums[i]
        #     num += 1
        # return(res)
            
