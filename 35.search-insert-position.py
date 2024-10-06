class Solution:
    # binary search example
    def searchInsert(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            middle = (start + end) // 2
            middleValue = nums[middle]
            if middleValue == target:
                return middle
            elif middleValue < target:
                start = middle + 1
            else:
                end = middle - 1
        return start
