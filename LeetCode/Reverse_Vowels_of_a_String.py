class Solution:
    def reverseVowels(self, s: str) -> str:

        l = "aAeEiIoOuU"

        start = 0
        end = len(s)-1

        s = list(s)

        while start < end:
            if s[start] in l and s[end] in l:

                temp = s[start]
                s[start] = s[end]
                s[end] = temp
                start +=1
                end -=1
            elif s[start] not in l:
                start +=1
            elif s[end] not in l: 
                end -=1
        return ''.join(s)


