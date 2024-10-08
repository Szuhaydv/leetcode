class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i, _ in enumerate(digits):
            if digits[-1 - i] == 9:
                digits[-1 - i] = 0
            else:
                digits[-1 - i] += 1
                return digits
        return [1] + digits



