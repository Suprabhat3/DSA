# This is my answer that have high time complexity becouse of two loops
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        num1 = []
        n = len(nums)
        k = k % n
        for i in range(n):
            if i < k:
                num1.append(nums[-1])
                nums.pop()

        num1.reverse()       
        for i in range(len(num1)):
            nums.insert(i, num1[i])


# GPT answer for faster results
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None
        """
        n = len(nums)
        k = k % n  # handle k > n

        # reverse whole list
        nums.reverse()
        # reverse first k elements
        nums[:k] = reversed(nums[:k])
        # reverse the remaining elements
        nums[k:] = reversed(nums[k:])



#check updated code here
