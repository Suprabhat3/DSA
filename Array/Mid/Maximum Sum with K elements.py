# You are given a **0-indexed** integer array `nums` and an integer `k`. Your task is to perform the following operation **exactly** `k` times in order to maximize your score:

# 1. Select an element `m` from `nums`.
# 2. Remove the selected element `m` from the array.
# 3. Add a new element with a value of `m + 1` to the array.
# 4. Increase your score by `m`.

# Return *the maximum score you can achieve after performing the operation exactly* `k` *times.*

class Solution(object):
    def maximizeSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        sum = 0
        for i in range (1,k+1):
            sum += nums[-1]
            temp = int(nums[-1])
            nums.pop()
            nums.append(temp+1)
        return sum    
        
            
