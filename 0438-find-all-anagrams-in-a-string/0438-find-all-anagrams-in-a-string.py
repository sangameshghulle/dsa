class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        lookup={}
        window={}
        len1=0
        left=0
        ans=[]
        for i in p:
            lookup[i]=lookup.get(i,0)+1
        for i in range(len(s)):
            window[s[i]]=window.get(s[i],0)+1
            if(i-left+1>len(p)):
                window[s[left]]-=1
                if(window[s[left]]==0):
                    del window[s[left]] 
                left+=1
            if(lookup==window):
                ans.append(left)
        return ans            