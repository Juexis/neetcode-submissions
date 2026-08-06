class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        allUniqueValues = set()
        for number in nums:
            allUniqueValues.add(number)
        

        if len(allUniqueValues) < len(nums):
            return True
        else:
            return False

            