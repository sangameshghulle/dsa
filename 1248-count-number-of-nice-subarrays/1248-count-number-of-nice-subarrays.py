class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        def sub(k):    
            l,r=0,0
            n=len(nums)
            count=0
            odds=0
            while r<n:
                if nums[r]%2!=0:
                    odds+=1
                while odds>k:
                    if nums[l]%2!=0:
                        odds-=1 
                    l+=1
                count+=r-l+1
                r+=1
            return count
        
        return sub(k)-sub(k-1)

        