from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        dict_numbers = Counter(arr)
        occurences = []
        for key, value in dict_numbers.items():
            print(value)
            if value not in occurences:
                occurences.append(value)
            else:
                return False
        return True


solution = Solution()
arr = [1,2,2,1,1,3]
print(solution.uniqueOccurrences(arr))