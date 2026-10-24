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

        fibs=[0]*(n+1)
        fibs[0]=0
        fibs[1]=1

        for i in range(2,n+1):
            fibs[i]=fibs[i-1]+fibs[i-2]
        
        return fibs[n]