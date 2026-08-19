class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        freq={}
        n=len(fruits)
        l,r=0,0
        ans=0
        for r,num in enumerate(fruits):
            freq[num]=freq.get(num,0)+1
            while len(freq)>2:
                freq[fruits[l]]=freq.get(fruits[l])-1
                if freq[fruits[l]]==0:
                    del freq[fruits[l]]
                l+=1
            curr=r-l+1
            if curr>ans:
                ans=curr

        return ans 