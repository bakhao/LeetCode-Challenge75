class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        pointer_word1 = 0
        pointer_word2 = 0
        result = ''
        if len(word1) == len(word2):
            while pointer_word1 < len(word1):
                result += word1[pointer_word1]
                result += word2[pointer_word1]
                pointer_word1 += 1
        elif len(word1) < len(word2):
            while pointer_word1 < len(word1):
                result += word1[pointer_word1]
                result += word2[pointer_word2]
                pointer_word1 += 1
                pointer_word2 += 1
            result = result + word2[pointer_word2:]
        else:
            while pointer_word2 < len(word2):
                result += word1[pointer_word1]
                result += word2[pointer_word2]
                pointer_word1 += 1
                pointer_word2 += 1
            result = result + word1[pointer_word1:]
        return result







solution = Solution()

word1 = "abc"
word2 = "pqr"

print(solution.mergeAlternately(word1, word2))