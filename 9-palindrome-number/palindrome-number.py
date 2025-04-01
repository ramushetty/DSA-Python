class Solution:
    def isPalindrome(self, x: int) -> bool:
        dup = x
        rev_num = 0
        while dup > 0:
            ld = dup % 10
            rev_num = (rev_num*10)+ ld
            dup = dup//10
        return rev_num == x
        