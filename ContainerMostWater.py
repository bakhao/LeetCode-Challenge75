class Solution:
    def maxArea(self, height: list[int]) -> int:
        i = 0
        j = len(height) - 1
        maximumArea = 0
        while i < j:
            area = (j-i)*min(height[i], height[j])
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
            if area > maximumArea:
                maximumArea = area
        return maximumArea


solution = Solution()
height = [1,8,6,2,5,4,8,3,7]
print(solution.maxArea(height))