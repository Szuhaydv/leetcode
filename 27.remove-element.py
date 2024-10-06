class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # solving with "2 pointers"
        # one keeps track of last written element, another traverses the list
        last_fixed = 0
        for num in nums:
            if num != val:
                nums[last_fixed] = num
                last_fixed += 1
        return last_fixed

