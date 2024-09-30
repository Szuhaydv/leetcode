# using a simple map for pair lookup
class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []
        bracketPairs = {"(":")", "[":"]", "{":"}"}

        for bracket in s:
            if bracket in bracketPairs:
                brackets.append(bracket)
            else:
                if not brackets or bracketPairs[brackets[-1]] != bracket:
                    return False
                else:
                    brackets.pop()
        if not brackets:
            return True
        else:
            return False
