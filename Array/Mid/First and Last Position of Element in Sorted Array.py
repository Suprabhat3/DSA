# 34. Find First and Last Position of Element in Sorted Array

# This Question is solve using Binary Search

class Solution(object):
    def searchRange(self, nums, target):
        def findFirst(nums, target):
            start, end = 0, len(nums) - 1
            first = -1
            while start <= end:
                mid = (start + end) // 2
                if nums[mid] == target:
                    first = mid
                    end = mid - 1  # search left
                elif nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            return first

        def findLast(nums, target):
            start, end = 0, len(nums) - 1
            last = -1
            while start <= end:
                mid = (start + end) // 2
                if nums[mid] == target:
                    last = mid
                    start = mid + 1  # search right
                elif nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            return last

        first = findFirst(nums, target)
        last = findLast(nums, target)
        return [first, last]
