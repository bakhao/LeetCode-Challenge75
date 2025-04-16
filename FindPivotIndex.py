import math


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        indexTarget = float('inf')
        for i in range(len(nums)):
            listSumLeft = nums[:i]
            listSumRight = nums[i+1:]
            if listSumLeft and listSumRight:
                sumLeft = sum(listSumLeft)
                sumRight = sum(listSumRight)
                if sumLeft == sumRight:
                    indexTarget = i
                    break
            if not listSumLeft:
                sumRight = sum(listSumRight)
                if sumRight == 0:
                    indexTarget = 0
                    break
            if not listSumRight:
                sumLeft = sum(listSumLeft)
                if sumLeft == 0:
                    indexTarget = i
                    break
        if indexTarget == float('inf'):
            return -1
        else:
            return indexTarget



solution = Solution()
nums = [-1,-1,0,1,1,0]
print(solution.pivotIndex(nums))