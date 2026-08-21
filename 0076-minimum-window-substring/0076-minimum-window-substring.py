class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s==t:
            return s
        ans=s+t
        l,r=0,0
        n=len(s)
        countT=Counter(t)
        countS=Counter()
        while l<=r<n:
            countS[s[r]]=countS.get(s[r],0)+1
            while countS>=countT:
                if len(ans)>r-l+1:
                    ans=s[l:r+1]
                countS[s[l]]-=1
                if countS[s[l]]==0:
                    del countS[s[l]]
                l+=1

            r+=1
        
                
        return ans if ans!=s+t else ""