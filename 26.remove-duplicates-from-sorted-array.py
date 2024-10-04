class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        uniques = {}
        last_sorted_id = -1
        for i, val in enumerate(nums):
                # could use convenience function: nums.remove(nums[i])
                # A bit more revealing:
            if val not in uniques:
                nums[last_sorted_id + 1] = val
                last_sorted_id += 1
                uniques[val] = True
        return len(uniques)

