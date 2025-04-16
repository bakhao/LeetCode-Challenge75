import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        size_str1 = len(str1)
        size_str2 = len(str2)
        gcd_both_str = math.gcd(size_str1, size_str2)
        target = str1[0:gcd_both_str]
        if (str1 + str2) == (str2 + str1):
            return target
        else:
            return ''





solution = Solution()

str1 = "ABCABC"
str2 = "ABC"

print(solution.gcdOfStrings(str1, str2))



#print(solution.convert_set_string(['ABC', 'ABC']))