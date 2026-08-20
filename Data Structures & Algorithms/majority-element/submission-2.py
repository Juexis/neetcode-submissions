class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        major_threshold: int = len(nums) // 2 # // is a shortcut for floor

        majority: int = nums[0] # set default so frequency[majority] doesn't check key "0"
        frequency: dict = {} # frequency map for numbers in nums

        # go through nums[] and add the numbers (keys) and the amount of appearances (values)
        for number in nums:
            frequency[number] = 1 + frequency.get(number, 0)
        
        for key in frequency:
            if frequency.get(key, 0) >= major_threshold: # frequency.get(key,0) to get the value of a key
                if frequency.get(key, 0) > frequency[majority]: # compare the frequency of the current key to the frequency of the majority key
                    majority = key

        return majority

