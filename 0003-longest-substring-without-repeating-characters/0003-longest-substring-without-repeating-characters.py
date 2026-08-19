class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans=0
        l=0
        n=len(s)
        seen={}
        for r,ch in enumerate(s):
            if ch in seen and seen[ch]>=l:
                l=seen[ch]+1
            currlen=r-l+1
            if currlen>ans:
                ans=currlen
            seen[ch]=r
            
        return ans