class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) # creating a dictionary of lists

        for s in strs:
            key: str = ''.join(sorted(s))
            
            result[key].append(s)
        
        return list(result.values())
        