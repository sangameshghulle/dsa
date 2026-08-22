class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        l,r,mid=0,n-1,n//2
        while l<=r:
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                l=mid+1
                
            else:
                r=mid-1

            mid=l+(r-l)//2
            # print(l,mid,r)

        return -1