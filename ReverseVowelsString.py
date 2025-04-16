class Solution:
    def reverseVowels(self, s: str) -> str:
        index_left = 0
        index_right = len(s)-1
        s_list = list(s)
        vowels = ['a', 'e', 'i', 'o', 'u', 'I', 'A', 'E', 'O', 'U',]
        while index_left < index_right:
            if s_list[index_left] in vowels and s_list[index_right] in vowels:
                self.swap_leeter(index_left, index_right, s_list)
                index_left += 1
                index_right -= 1
            elif s_list[index_left] not in vowels:
                index_left += 1
            elif s_list[index_right] not in vowels:
                index_right -= 1
        return ''.join(i for i in s_list)


    def swap_leeter(self, i, j, data):
        tmp = data[i]
        data[i] = data[j]
        data[j] = tmp
        return data

solution = Solution()
s = "IceCreAm"

target = "AceCreIm"
print(solution.reverseVowels(s))
