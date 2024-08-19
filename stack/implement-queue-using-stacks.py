class MyQueue(object):

    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []
        #self.size = len(stack_1) + len(stack_2)
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack_1.append(x)
        #self.size +=1
        

    def pop(self):
        """
        :rtype: int
        """
        if len(self.stack_1) > 0 and len(self.stack_2) == 0:
            while self.stack_1:
                self.stack_2.append(self.stack_1.pop())
        return self.stack_2.pop() 

    def peek(self):
        """
        :rtype: int
        """
        if len(self.stack_1) > 0 and len(self.stack_2) == 0:
            while self.stack_1:
                self.stack_2.append(self.stack_1.pop())
        item = self.stack_2.pop()
        self.stack_2.append(item)
        return item
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack_1) + len(self.stack_2)== 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()