class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atmost(k):
            ans=0
            l,r=0,0
            n=len(nums)
            freq={}
            while r<n:
                freq[nums[r]]=freq.get(nums[r],0)+1
                while len(freq)>k:
                    freq[nums[l]]-=1
                    if freq[nums[l]]==0:
                        del freq[nums[l]]
                    l+=1
                ans+=r-l+1
                r+=1
            return ans
        return atmost(k)-atmost(k-1)