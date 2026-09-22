class FreqStack:

    def __init__(self):
        self.freq = {}       # value -> frequency
        self.groups = {}     # frequency -> stack of values
        self.max_freq = 0

    def push(self, val: int) -> None:
        self.freq[val] = self.freq.get(val, 0) + 1
        f = self.freq[val]

        if f > self.max_freq:
            self.max_freq = f

        if f not in self.groups:
            self.groups[f] = []

        self.groups[f].append(val)

    def pop(self) -> int:
        val = self.groups[self.max_freq].pop()

        self.freq[val] -= 1

        if not self.groups[self.max_freq]:
            self.max_freq -= 1

        return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()