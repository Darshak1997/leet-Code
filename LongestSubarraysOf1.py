class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        k = 1
        i = 0
        for j in range(len(nums)):
            k -= nums[j] == 0
            if k < 0:
                k += nums[i] == 0
                i += 1
        return j - i
#         res = [0]*len(nums)
#         self.flag = True
#         self.pos = 0
#         for i in range(len(nums)):
#             if nums[i] == 0:
#                 res[i] = 0
#             elif nums[i] == 1:
#                 count = self.recc(nums[i:], 0, res)
#                 self.flag = True
#                 # res[i] = count
#                 print(res)
#         print("Res: ", res )
#         if max(res) == len(res):
#             return max(res)-1
#         return(max(res))
    
#     def recc(self, nums, count, res):
#         print("Nums: ", nums)
#         if nums == []:
#             return count
#         if nums[0] == 0 and len(nums) == 1:
#             return count
#         if nums[0] == 1:
#             print("If: ", count+1)
#             return self.recc(nums[1:], count + 1, res)
#         elif (nums[0] == 0 and nums[1] == 1) and (self.flag == True):
#             self.flag = False
#             print("elif: ", count+1)
#             return self.recc(nums[2:], count+1, res)
#         else:
#             return self.recc(nums[1:], count, res)
        
