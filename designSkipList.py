class Node:
    __slots__ = 'val', 'levels'
    def __init__(self, val, levels):
        self.levels = [None]*levels
        self.val = val

class Skiplist:

    def __init__(self):
        self.head = Node(-1, 16)
    
    def _iter(self, num):
        curr = self.head
        for level in reversed(range(15)):
            while True:
                future = curr.levels[level]
                if future and future.val < num:
                    curr = future
                else:
                    break
            yield curr, level

    def search(self, target: int) -> bool:
        for prev, level in self._iter(target):
            pass
        curr = prev.levels[0]
        return curr and curr.val == target

    def add(self, num: int) -> None:
        nodelvls = min(16, 1 + int(math.log2(1.0 / random.random())))
        node = Node(num, nodelvls)
        
        for cur, level in self._iter(num):
            if level < nodelvls:
                future = cur.levels[level]
                cur.levels[level] = node
                node.levels[level] = future

    def erase(self, num: int) -> bool:
        ans = False
        for cur, level in self._iter(num):
            future = cur.levels[level]
            if future and future.val == num:
                ans = True
                cur.levels[level] = future.levels[level]
        return ans


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
