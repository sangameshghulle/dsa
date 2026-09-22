class FreqStack:

    def __init__(self):
        self.freq = {}       # value -> frequency
        self.groups = {}     # frequency -> stack of values
        self.max_freq = 0

    def push(self, val: int) -> None:
        self.freq[val]=self.freq.get(val,0)+1
        freq=self.freq[val]
        if freq>self.max_freq:
            self.max_freq=freq
        if freq not in self.groups:
            self.groups[freq]=[]
        self.groups[freq].append(val)
        
    def pop(self) -> int:
        val=self.groups[self.max_freq].pop()
        self.freq[val]-=1
        if self.freq[val]==0:
            del self.freq[val]
        if not self.groups[self.max_freq]:
            self.max_freq-=1
        return val
        
        

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()