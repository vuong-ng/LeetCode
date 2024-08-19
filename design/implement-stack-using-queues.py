class MyStack(object):

    def __init__(self):
        self.queue = []
        self.size = len(self.queue)

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue.append(x)
        self.size +=1 
        

    def pop(self):
        """
        :rtype: int
        """
        if self.size > 0:
            self.size -=1
            return self.queue.pop()
        else:
            return 0
        

    def top(self):
        """
        :rtype: int
        """
        return self.queue[-1]

    def empty(self):
        """
        :rtype: bool
        """
        if self.size == 0:
            return True
        else: return False

        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()