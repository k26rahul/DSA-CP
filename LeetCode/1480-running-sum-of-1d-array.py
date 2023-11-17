from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]

        return nums


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        results = [nums[0]] + [0] * (len(nums) - 1)
        for i in range(1, len(nums)):
            results[i] = nums[i] + results[i - 1]

        return results


print(Solution().runningSum([1, 2, 3, 4]))
