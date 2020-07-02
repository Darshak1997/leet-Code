class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        count = [0]*k
        for num in arr:
            count[num%k] +=1
        i, j = 1, k-1
        pairs = 0
        while i < j:
            if count[i] != count[j]:
                return False
            pairs += count[i]
            i += 1
            j -= 1
        if pairs>0 and i==j:
            pairs += count[i]/2
        pairs += count[0]/2
        n = len(arr)
        return pairs == n//2
