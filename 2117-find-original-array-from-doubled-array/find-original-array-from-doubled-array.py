class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed_length = len(changed)
        if changed_length % 2 != 0:
            return []
        
        mapp = {}
        changed.sort()
        for element in changed:
            mapp[element] = mapp.get(element,0) + 1
        result = []
        for element in changed:
            twice = element*2
            if mapp[element] == 0:
                continue
            if mapp.get(twice,0) == 0:
                return []
            
            result.append(element)
            mapp[element] -= 1
            mapp[twice] -= 1

        return result

        