class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        postfix=[]
        op=[]

        i=0
        n=len(s)

        priority = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2
        }

        while i<n:
            if s[i]==' ':
                i+=1
                continue
            if s[i].isdigit():
                num=0
                while i<n and s[i].isdigit():
                    num=num*10+int(s[i])
                    i+=1
                postfix.append(num)
                continue

            elif s[i]=='(':
                op.append(s[i])

            elif s[i]==')':
                while op and op[-1]!='(':
                    postfix.append(op.pop())
                op.pop()

            elif s[i] in '+-*/':
                current_op=s[i]

                while op and priority[op[-1]] >= priority[current_op]:
                    postfix.append(op.pop())
                op.append(current_op)
            i+=1
        while op:
            postfix.append(op.pop())
        

        stack=[]
        for x in postfix:
            if isinstance(x,int):
                stack.append(x)
            elif x=='/':
                b=stack.pop()
                a=stack.pop()
                stack.append(int(a/b))

            elif x=='*':
                stack.append(stack.pop()*stack.pop())
            elif x=='+':
                stack.append(stack.pop()+stack.pop())
            else:
                stack.append(-stack.pop()+stack.pop())

        return int(stack[-1])