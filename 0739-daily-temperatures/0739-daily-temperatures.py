class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        result=[0]*n
        stack=[]
        for i in range(n):
            while stack and temperatures[stack[-1]]<temperatures[i]:
                smaller=stack.pop()
                result[smaller]=i-smaller
            stack.append(i)

        return result