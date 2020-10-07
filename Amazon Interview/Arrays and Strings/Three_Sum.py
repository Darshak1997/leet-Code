class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.findTriplets(-nums[i], i+1, triplets, nums)
            
        return triplets
    
    def findTriplets(self, target, start, triplets, nums):
        end = len(nums) - 1
        
        while start < end:
            currSum = nums[start]+nums[end]
            if currSum == target:
                triplets.append([-target, nums[start], nums[end]])
                start += 1
                end -= 1
                while start < end and nums[start] == nums[start-1]:
                    start += 1
                while start < end and nums[end] == nums[end+1]:
                    end -= 1
            elif currSum < target:
                start += 1
            else:
                end -= 1
            
