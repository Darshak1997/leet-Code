class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.currSize = 0
        self.MaxSize = k
        self.queue = [0]*k
        self.head = self.tail = -1

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.currSize < self.MaxSize:
            if self.tail == -1:
                self.head = self.tail = 0
            else:
                self.tail = (self.tail + 1)%self.MaxSize
            self.queue[self.tail] = value
            self.currSize += 1
            return True
        else:
            return False

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.currSize == 0: return False
        if self.head == self.tail:
            self.head = self.tail = -1
        else:
            self.head = (self.head + 1)%self.MaxSize
        self.currSize -= 1
        return True
        

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.currSize != 0:
            return self.queue[self.head]
        else:
            return -1

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.currSize != 0:
            return self.queue[self.tail]
        else:
            return -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        if self.currSize == 0:
            return True
        else:
            return False

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        if self.currSize == self.MaxSize:
            return True
        else:
            return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
