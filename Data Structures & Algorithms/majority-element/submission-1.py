class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        major_threshold: int = math.floor(len(nums) / 2)

        majority: int = 0
        frequency: dict = {} # frequency map for numbers in nums
        
        frequency[0] = 0
        
        # go through nums[] and add the numbers (keys) and the amount of appearances (values)
        for number in nums:
            frequency[number] = 1 + frequency.get(number, 0)

            # print (str(number) + ": " + str(frequency[number]))
        
        for key in frequency:
            if frequency.get(key, 0) >= major_threshold: # key refers to the value
                if frequency.get(key, 0) > frequency[majority]: # compare the frequency of the current key to the frequency of the majority key
                    majority = key

        return majority

