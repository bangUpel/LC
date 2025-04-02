class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_num = str(x)
        reversed_num = str_num[::-1]
        return str_num == reversed_num
            
        
