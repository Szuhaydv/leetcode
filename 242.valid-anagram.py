def fillHashmap(string):
    dict = {}
    for letter in string:
        if letter in dict:
            dict[letter] += 1
        else:
            dict[letter] = 1
    return dict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        hmap1 = fillHashmap(s)
        hmap2 = fillHashmap(t)
        for key in hmap1:
            if key not in hmap2:
                return False
            if hmap1[key] != hmap2[key]:
                return False
        return True
