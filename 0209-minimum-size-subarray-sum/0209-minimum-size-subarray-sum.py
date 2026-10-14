class Solution(object):
    def minSubArrayLen(self, target, nums):

        left = 0
        total = 0
        min_length = float("inf")

        for right in range(len(nums)):

            total += nums[right]   #expand the window

            while total >= target:  # start shrinking 
                
                min_length = min(min_length, right-left+1)  #store smallest window

                total -= nums[left]  # remove left
                left += 1  #move left 

        if min_length == float("inf"):
            return 0

        return min_length