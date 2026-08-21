class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s==t:
            return s
        ans_st=0
        l=0
        ans_len=float('inf')
        need=Counter(t)
        required=len(need)
        window={}
        formed=0
        for r in range(len(s)):
            char=s[r]
            window[char]=window.get(char,0)+1

            if char in need and window[char]==need[char]:
                formed+=1
            
            while formed==required:

                if ans_len>r-l+1:
                    ans_len=r-l+1
                    ans_st=l
                
                leftchar=s[l]
                l+=1

                window[leftchar]-=1
                
                if leftchar in need and window[leftchar]<need[leftchar]:
                    formed-=1
        
        if ans_len==float('inf'):
            return ""

        return s[ans_st:ans_st+ans_len]