class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        l,r=0,n-1
        ans=[0]*n
        k=n
        while l<=r:
            x,y=nums[l]**2,nums[r]**2
            k-=1
            if x>y:
                ans[k]=x
                l+=1
            else:
                ans[k]=y
                r-=1
        return ans