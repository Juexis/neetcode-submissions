class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        result: str = ""

        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]: # can access the word and index the letter
                    return result
            
            # if all words in strs have the same letter at the current index, we can add that letter to the result
            result += strs[0][i]
        return result
