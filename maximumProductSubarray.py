class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = -float('inf')
        product = 1
        length = len(nums)
        for i in range(length):
            product *= nums[i]
            res = max(product, res)
            if nums[i] == 0:
                product = 1
        # scan backward
        product = 1
        for j in range(length - 1, -1, -1):
            product *= nums[j]
            res = max(product, res)
            if nums[j] == 0:
                product = 1
        return res
        # maxArr = []
        # for start in range(len(nums)):
        #     currMax = -inf
        #     end = start + 1
        #     currProduct = nums[start]
        #     # currMax = max(currMax, currProduct)
        #     currMax = currProduct
        #     while end <= len(nums)-1:
        #         currMax = max(currMax, currProduct)
        #         currProduct *= nums[end]
        #         end += 1
        #     maxArr.append(currMax)
        # return max(maxArr)
