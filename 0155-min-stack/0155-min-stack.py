class MinStack:

    def __init__(self):
        self.stack=[]
        # self.min_stack=[]
        self.min=99999999999999999999
        

    def push(self, value: int) -> None:
        self.stack.append(value)
        # if not self.min_stack:
        #     self.min_stack.append(value)
        # else:
        #     self.min_stack.append(min(value,self.min_stack[-1]))
        if self.min>value:
            self.min=value
        

    def pop(self) -> None:
        value=self.stack.pop()
        # self.min_stack.pop()
        if value==self.min:
            self.min=min(self.stack) if self.stack else 99999999999999999999
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min
        # return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()