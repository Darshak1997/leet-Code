class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # TC: O(n) SC: O(n)
        count = 0
        sums = 0
        d = dict()
        d[0] = 1
        
        for i in range(len(nums)):
            sums += nums[i]
            count += d.get(sums-k, 0)
            d[sums] = d.get(sums, 0)+1
        print(d)
        return(count)
        
        # TC: O(n^2) SC: O(n)
        count = 0
        res = [0]*(len(nums))
        for i in range(1, len(nums)):
            res[i] = res[i-1] + nums[i-1]
        for start in range(len(nums)):
            for end in range(start+1, len(nums)):
                if res[end] - res[start] == k:
                    count += 1
        print(res)
        return(count)
