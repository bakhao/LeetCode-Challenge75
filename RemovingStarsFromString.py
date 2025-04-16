class Solution:
    def removeStars(self, s: str) -> str:
        stacks = []
        for character in s:
            if character == '*' and stacks:
                stacks.pop()
            else:
                stacks.append(character)
        result = ''.join([i for i in stacks])
        return result


solution = Solution()
s = ""
print(solution.removeStars(s))