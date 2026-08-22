class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        sum=0
        ans=0

        l=0
        r=0
        n=len(nums)
        window=set()

        while l<=r<n:
            while nums[r] in window:
                num=nums[l]
                sum-=num
                window.remove(num)
                l+=1
            num=nums[r]
            sum+=num
            window.add(num)
            if ans<sum:
                ans=sum
            r+=1
        
        return ans
