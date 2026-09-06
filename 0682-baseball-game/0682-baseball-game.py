class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # score=0
        stack=[]
        for  op in operations:
            if op=='C':
                stack.pop()
                # print(stack)
            elif op=='D':
                a=stack[-1]*2
                stack.append(a)
                # print(stack)
            elif op=='+':
                a=stack[-1]+stack[-2]
                stack.append(a)
                # print(stack)
            else:
                stack.append(int(op))
                # print(stack)
        # print(stack)

        return sum(stack)