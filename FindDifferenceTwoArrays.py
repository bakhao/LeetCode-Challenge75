class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:

        num1_without_num2 = []
        num2_without_num1 = []
        for num1 in set(nums1):
            if num1 not in nums2:
                num1_without_num2.append(num1)

        for num2 in set(nums2):
            if num2 not in nums1:
                num2_without_num1.append(num2)
        return [num1_without_num2, num2_without_num1]


solution = Solution()

nums1 = [1,2,3]
nums2 = [2,4,6]

print(solution.findDifference(nums1, nums2))