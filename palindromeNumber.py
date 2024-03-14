class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_number=str(x)
        if str_number==str_number[::-1]:
            return True
        else:
            return False