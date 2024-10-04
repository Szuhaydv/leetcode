class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # No need for dict to store uniques
        # you are comparing to the last fixed item
        last_sorted_id = 0
        for i in range(1, len(nums)):
                # could use convenience function: nums.remove(nums[i])
                # A bit more revealing:
            if nums[i] != nums[last_sorted_id]:
                nums[last_sorted_id + 1] = nums[i]
                last_sorted_id += 1
        return last_sorted_id + 1

