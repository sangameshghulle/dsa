class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n=len(letters)
        l,r,ans=0,n-1,0
        while l<=r:
            mid=(l+r)//2
            if letters[mid]>target:
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return letters[ans]