class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # both strings need to be same length to be a valid anagram
        if len(s) != len(t):
            return False

        countS = {} # making dictionaries/hash map
        countT = {}

        for i in range(len(s)):
            # creates a key for the current letter in s, adds one to its value if the key already exists, if not then it adds 1 to 0
            countS[s[i]] = 1 + countS.get(s[i], 0)

        for i in range(len(t)):
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        for c in countS:
            if countS.get(c, 0) != countT.get(c, 0): # .get(key, default) returns the value given the key
                return False
        
        return True