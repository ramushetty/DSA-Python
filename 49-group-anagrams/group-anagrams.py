class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h_map = {}
        for word in strs:
            char_array = [0]*26
            for c in word:
                char_array[ord(c)-ord('a')] +=1
            new_word = ''
            for i in range(26):
                if  char_array[i] > 0:
                    temp = chr(ord('a')+i)
                    for c in range(char_array[i]):
                        new_word+=temp
            if new_word in h_map:
                h_map[new_word].append(word)
            else:
                h_map[new_word] = [word]

        result = []
        for item in h_map.items():
            result.append(item[1])
        return result 