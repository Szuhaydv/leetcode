class Solution:
    # time complexity: O(n * m) - if n,m are the length of haystack, needle
    def strStr(self, haystack: str, needle: str) -> int:
        for i, val in enumerate(haystack):
            if val == needle[0]:
                if haystack[i:i+len(needle)] == needle:
                    return i
        return -1

