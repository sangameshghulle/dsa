# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l,r,mid=1,n,n//2
        while l<=r:
            if isBadVersion(mid):
                r=mid-1
            else:
                l=mid+1
            mid=l+(r-l)//2
        
        return l
        