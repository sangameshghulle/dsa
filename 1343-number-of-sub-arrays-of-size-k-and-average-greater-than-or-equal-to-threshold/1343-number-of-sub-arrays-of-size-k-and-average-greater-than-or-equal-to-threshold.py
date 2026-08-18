class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans=0
        n=len(arr)
        threshold*=k
        window=sum(arr[:k])
        if window>=threshold:
            ans+=1
        for i in range(k,n):
            window=arr[i]+window-arr[i-k]
            if window>=threshold:
                ans+=1
        return ans