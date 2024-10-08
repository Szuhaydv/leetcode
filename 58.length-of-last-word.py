class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word_end_id = -1
        for i in range(len(s)):
            current_id = len(s) - 1 - i
            if s[current_id] != " ":
                if word_end_id == -1:
                    word_end_id = current_id
            elif word_end_id != -1:
                return word_end_id - current_id
        return word_end_id + 1
