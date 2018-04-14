class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        temp = set(nums)

        if(len(nums) == len(temp)):
            return False #no duplicates
        else:
            return True #duplicates exist
