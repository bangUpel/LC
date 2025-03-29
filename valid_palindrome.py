class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = ''.join(char.lower() for char in s if char.isalnum())
        if new_string == new_string[::-1]:
            return True
        else:
            return False
