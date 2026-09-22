class Solution:
    def minInsertions(self, s: str) -> int:
        insertions = 0

        stack=[]

        i=0
        n=len(s)

        while i<n:
            if s[i]=='(':
                stack.append(s[i])
                i+=1
            
            else:
                if not stack:
                    insertions+=1
                    stack.append('(')
                
                i+=1

                if i<n and s[i]==')':
                    i+=1
                else:
                    insertions+=1
                
                stack.pop()
        
        insertions+=2*len(stack)

        return insertions
