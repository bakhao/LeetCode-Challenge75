class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_zeros = 0
        pointer_insertion = 0
        for i in range(len(nums)):
            if nums[i] != 0:
              nums[pointer_insertion] = nums[i]
              pointer_insertion += 1
            else:
                count_zeros += 1
        for i in range(pointer_insertion, len(nums)):
            nums[i] = 0
        print(count_zeros)
        return nums

    def swap_leeter(self, i, j, data):
        tmp = data[i]
        data[i] = data[j]
        data[j] = tmp
        return data


solution = Solution()
nums = [0,1,0,3,12]
print(solution.moveZeroes(nums))