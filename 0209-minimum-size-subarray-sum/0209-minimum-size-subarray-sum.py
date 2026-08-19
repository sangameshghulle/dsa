class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans=float('inf')
        l=0
        window=0
        n=len(nums)
        r=0
        while r<n:
            window+=nums[r]
            while window>=target:
                ans=min(ans,r-l+1)
                window-=nums[l]
                l+=1
            
            r+=1

        return ans if ans!=float('inf') else 0