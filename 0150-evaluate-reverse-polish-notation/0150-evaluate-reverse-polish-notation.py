class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for t in tokens:
            if t in {"/","*","+","-"}:
                b=stack.pop()
                a=stack.pop()
                if t=='/':
                    stack.append(int(a/b))
                    # print(int(a/b),stack)
                elif t=='+':
                    stack.append(a+b)
                    # print(a+b,stack)
                elif t=='-':
                    stack.append(a-b)
                    # print(a-b,stack)
                else:
                    stack.append(a*b)
                    # print(a*b,stack)
            else:
                # print("added ",t)
                stack.append(int(t))
        # print(stack)
        return stack[-1]