class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict = {}
        l, r = 0, 0
        longest_string = 0
        while r < len(s):
            if s[r] not in dict:
                dict[s[r]] = r
                if r - l + 1 > longest_string:
                    longest_string = r - l + 1
            else:
                last_occurence = dict[s[r]]
                for i in range(l, last_occurence):
                    dict.pop(s[i])
                l = last_occurence + 1
                dict[s[r]] = r
            r += 1
        return longest_string

