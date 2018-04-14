class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = 0
        final_index = len(nums)
        while index < final_index:
            if index == 0:
                pass
            elif(nums[index] == nums[index-1]):
                nums.pop(index)
                index = index - 1
                final_index = final_index - 1

            index += 1


        return len(nums)
