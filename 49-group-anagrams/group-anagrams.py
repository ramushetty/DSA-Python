class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h_map = {}
        print(strs)
        for word in strs:
            temp = ''.join(sorted(word))
            # print(temp)

            if temp in h_map:
                h_map[temp].append(word)
            else:
                h_map[temp] = [word]
        result = []
        for item in h_map.items():
            result.append(item[1])
        return result
        