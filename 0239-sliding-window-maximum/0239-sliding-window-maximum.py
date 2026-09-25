from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        q = deque()   # stores indices
        result = []

        for i in range(len(nums)):

            # 1. Remove indices outside the current window
            while q and q[0] < i - k + 1:
                q.popleft()

            # 2. Remove smaller/equal values from the back
            #    They can never become the maximum again.
            while q and nums[q[-1]] <= nums[i]:
                q.pop()

            # 3. Add current index
            q.append(i)

            # 4. Window is complete -> front is maximum
            if i >= k - 1:
                result.append(nums[q[0]])

        return result