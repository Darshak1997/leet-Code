# s = "leetcode"
# return 0.

# s = "loveleetcode",
# return 2.


class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s)
        print(count)
        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx     
        return -1
