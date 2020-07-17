class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter, visited, stack = collections.Counter(s), set(), []
        
        for ch in s:
            counter[ch] -= 1
            if ch in visited:   continue
            while stack and stack[-1] > ch and counter[stack[-1]] > 0:
                visited.remove(stack.pop())
            stack.append(ch)
            visited.add(ch)
                
        return "".join(stack)
        
    
