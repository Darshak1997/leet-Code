class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {"2": ["a","b","c"], "3": ["d","e","f"], "4":["g","h","i"], "5":["j","k","l"],
                  "6":["m","n","o"], "7": ["p","q","r","s"], "8":["t","u","v"], "9": ["w","x","y","z"]}
        arr = []
        if len(digits) == 0:
            return arr
        def backtrack(s, digit):
            if len(digit) == 0:
                arr.append(s)
            # s = ""
            else:
                for i in mapping[digit[0]]:
                    # print(s+i)
                    # s=s+i
                    backtrack(s+i, digit[1:])
        backtrack("", digits)
        return arr
