class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        lookup={}
        max_freq=0
        l,r=0,0
        n=len(s)
        ans=0

        while r<n:
            lookup[s[r]]=lookup.get(s[r],0)+1
            max_freq = max(max_freq, lookup[s[r]])
            while r-l+1-max_freq>k:
                lookup[s[l]]-=1
                l+=1

            if r-l+1-max_freq<=k:
                ans=max(ans,r-l+1)
            r+=1

        return ans
