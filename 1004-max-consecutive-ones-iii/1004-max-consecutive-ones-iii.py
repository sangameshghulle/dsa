class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ans=0
        count=0
        l,r=0,0
        n=len(nums)
        while r<n:
            if nums[r]==0:
                count+=1
            while count>k:
                if nums[l]==0:
                    count-=1
                l+=1
            curr=r-l+1
            if  curr>ans:
                ans=curr
            r+=1
        return ans