class Solution:
    # def __init__(self):
    #     self.memo={
    #         0:0,
    #         1:1
    #     }

    def fib(self, n: int) -> int:
        # if n in self.memo:
        #     return self.memo[n]
        # else:
        #     ans= self.fib(n-1)+self.fib(n-2)
        #     self.memo[n]=ans
        #     return ans
        if n<=1:
            return n

        prev1=1
        prev2=0

        for i in range(2,n+1):
            curr=prev1+prev2
            prev2=prev1
            prev1=curr
        
        return curr