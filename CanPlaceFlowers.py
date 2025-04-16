from collections import Counter

class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed)-1):
            previous = flowerbed[i-1]
            current = flowerbed[i]
            next = flowerbed[i+1]
            if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n -= 1
        if n <= 0:
            return True
        else:
            return False




solution = Solution()
flowerbed = [1,0,0,0,0,1]
n = 2
print(solution.canPlaceFlowers(flowerbed,n))