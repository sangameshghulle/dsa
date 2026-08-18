class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window=sum(nums[:k])
        n=len(nums)
        ans=window
        for i in range(k,n):
            window=window+nums[i]-nums[i-k]
            if window>ans:
                ans=window
        return ans/k