# original solution (checks if current symbol is "prependable"), bloated complexity
class SolutionOriginal:
    def romanToInt(self, s: str) -> int:
        valueMap = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        sum = 0
        i = 0
        while i < len(s):
            currentValue = valueMap[s[i]]
            nextValue = valueMap[s[i + 1]] if i + 1 < len(s) else 0

            if s[i] in {"I", "X", "C"}:
                if currentValue * 5 == nextValue or currentValue * 10 == nextValue:
                    sum += nextValue - currentValue
                    i += 1
                else:
                    sum += currentValue
            else:
                sum += currentValue
            i += 1
        return sum

# a lot easier if you realize you only need to check if next number is larger than the current one
class Solution:
    def romanToInt(self, s: str) -> int:
        valueMap = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = 0
        for i in range(len(s)):
            currentValue = valueMap[s[i]]
            nextValue = valueMap[s[i + 1]] if i + 1 < len(s) else 0

            if currentValue < nextValue:
                total -= currentValue
            else:
                total += currentValue
        return total

