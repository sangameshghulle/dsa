class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        if s=='':
            return ''
        stack=[]
        invalid=set()
        for i,ch in enumerate(s):
            if ch==')':
                if not stack:
                    invalid.add(i)
                else:
                    stack.pop()
                
            elif ch=='(':
                stack.append(i)
        
        while stack:
            invalid.add(stack.pop())
        
        ans=''
        for i,ch in enumerate(s):
            if i not in invalid:
                ans+=ch
        
        return ans