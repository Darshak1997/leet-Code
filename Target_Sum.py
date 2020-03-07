class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        count = collections.Counter({0: 1})
        for x in nums:
            step = collections.Counter()
            for y in count:
                step[y + x] += count[y]
                step[y - x] += count[y]
            count = step
        return count[S]
        
        
        # RECURSION #
#         self.count = 0
#         self.dfs(nums, 0, 0, S)
#         return self.count
    
#     def dfs(self, nums, i, Sum, target):
#         if i == len(nums):
#             if Sum == target:
#                 self.count += 1
#         else:
#             self.dfs(nums, i+1, Sum+nums[i], target)
#             self.dfs(nums, i+1, Sum-nums[i], target)
