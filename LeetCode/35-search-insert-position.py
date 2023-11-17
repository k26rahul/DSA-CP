# https://leetcode.com/problems/search-insert-position/

def searchInsert(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if nums[mid] == target:
            return mid

        elif nums[mid] < target:
            if low == high:
                return mid + 1
            low = mid + 1

        else:
            if low == high or mid == low:
                return mid
            high = mid - 1


print(searchInsert([1, 3, 5, 6], 5))  # 2
print(searchInsert([1, 3, 5, 6], 2))  # 1
print(searchInsert([1, 3, 5, 6], 7))  # 4
print(searchInsert([1, 3, 5, 6], 0))  # 0
print(searchInsert([3, 5, 7, 9, 10], 8))  # 0
