class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mapping = {}
        for i in nums:
            if i not in mapping:
                mapping[i] = 1
            else:
                mapping[i] = mapping[i]+1
        
        for item in mapping:
            if mapping[item] == 1:
                return item
