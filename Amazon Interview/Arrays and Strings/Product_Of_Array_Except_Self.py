class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]*len(nums)
        right = [1]*len(nums)
        answer = [1]*len(nums)
        
        # left[0] = 1
        for i in range(1, len(nums)):
            left[i] = left[i-1] * nums[i-1]
            
        # right[len(nums)-1] = 1
        for i in reversed(range(len(nums)-1)):
            right[i] = right[i+1] * nums[i+1]
            
        for i in range(len(nums)):
            answer[i] = left[i] * right[i]
        
        return answer
        # dp = []
        # for i in range(len(nums)):
        #     currProd = 1
        #     for j in range(len(nums)):
        #         if i != j:
        #             currProd = currProd * nums[j]
        #     dp.append(currProd)
        # return dp
