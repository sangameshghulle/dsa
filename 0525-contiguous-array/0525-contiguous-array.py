class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        lookup={0:-1}
        sum=0
        max_len=0

        for i in range(len(nums)):
            sum+=1 if nums[i]==1 else -1
            if sum in lookup:
                max_len=max(max_len,i-lookup[sum])
            else:
                lookup[sum]=i

        return max_len