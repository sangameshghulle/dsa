class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        # Find first occurrence
        l, r = 0, len(nums) - 1
        first = -1

        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] == target:
                first = mid
                r = mid - 1      # Search LEFT
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        # Find last occurrence
        l, r = 0, len(nums) - 1
        last = -1

        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] == target:
                last = mid
                l = mid + 1      # Search RIGHT
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return [first, last]