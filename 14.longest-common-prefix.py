# horizontal scanning of letters, no additional memory, just 'array splicing' the string
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for index, letter in enumerate(strs[0]):
            for word in strs:
                if index >= len(word) or word[index] != letter:
                    return word[0:index]
        return strs[0]
