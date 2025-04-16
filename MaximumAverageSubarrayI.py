import math


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        result = 0
        maxAverage = float('-inf')
        result = sum(nums[0:k])
        maxAverage = sum(nums[0:k])/k
        for i in range(0, len(nums) - k):
            result = (result - nums[i]) + nums[i + k]
            target = result / k
            if target > maxAverage:
                    maxAverage = target
        return maxAverage


solution = Solution()
nums = [1,12,-5,-6,50,3]
k = 4
print(solution.findMaxAverage(nums, k))

