class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) # creating a dictionary of lists

        for s in strs:
            key: list[int] = [0] * 26 # creates the key that anagrams will share
            for c in s:
                # using "a"'s ACSII value as a baseline, we can subtract a's ASCII value from the letter to find its distance from a, effectively finding its location in the alphabet
                key[ord(c) - ord("a")] += 1 
            
            result[tuple(key)].append(s)
        
        return list(result.values())