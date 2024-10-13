class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i, j = 0, 0
        dict = {nums[0]: 0}
        while j < len(nums) - 1:
            if j - i < k:
                j += 1
                if nums[j] in dict:
                    return True
                dict[nums[j]] = j
            else:
                dict.pop(nums[i])
                i += 1
        return False

