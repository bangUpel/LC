class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        return s == ''.join(char for char in t if char in s)
