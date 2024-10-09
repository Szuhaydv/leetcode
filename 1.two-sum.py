class Solution:
    # O(n) space and time
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, val in enumerate(nums):
            if target - val in dict:
                return [i, dict[target - val]]
            else:
                dict[val] = i
