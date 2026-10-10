class Solution(object):
    def removeDuplicates(self, nums):
        current = 0 
        k = 0

        while current < len(nums):
            if k < 2 or nums[current] != nums[k-2]:
                nums[k] = nums[current]
                k += 1
            current += 1
        return k
