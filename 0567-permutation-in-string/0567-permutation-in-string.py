class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1freq={}
        for k in s1:
            s1freq[k]=s1freq.get(k,0)+1
        
        s2freq={}
        s1len=len(s1)
        s2len=len(s2)
        for k in s2[:s1len]:
            s2freq[k]=s2freq.get(k,0)+1
        if s1freq==s2freq:
            return True
        for k in range(s1len,s2len):
            s2freq[s2[k]]=s2freq.get(s2[k],0)+1
            s2freq[s2[k-s1len]]-=1
            if s2freq[s2[k-s1len]]==0:
                del s2freq[s2[k-s1len]]
            if s1freq==s2freq:
                return True

        return False