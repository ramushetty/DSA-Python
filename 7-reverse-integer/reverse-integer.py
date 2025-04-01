class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            dup = -x
        else:
            dup = x
        rev_num = 0

        while dup > 0:
            ld = dup%10
            rev_num = (rev_num * 10)+ld
            dup = dup//10
        if rev_num > 2**31-1:
            return 0
        if x < 0:
            return -rev_num
        return rev_num
        