class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:

        result = []
        maxCandies = max(candies)
        for candie in candies:
            if (candie + extraCandies) >= maxCandies:
                result.append(True)
            else:
                result.append(False)
        return result