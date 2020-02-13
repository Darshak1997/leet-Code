# Input: [2,2,1]
# Output: 1


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashset = {}
        for i in nums:
            try:
                hashset.pop(i)
            except:
                hashset[i] = 1
        return hashset.popitem()[0]
