class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = {}
        for letter in ransomNote:
            letters[letter] = letters.get(letter, 0) + 1
        for letter in magazine:
            if letter in letters:
                letters[letter] = max(0, letters[letter] - 1)
        for value in letters.values():
            if value != 0:
                return False
        return True


