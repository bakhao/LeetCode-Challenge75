class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        gains_altitude = [0]
        start = 0
        for i in range(len(gain)):
            start = sum(gain[:i+1])
            gains_altitude.append(start)
        return max(gains_altitude)


solution = Solution()
gain = [-4,-3,-2,-1,4,3,2]
print(solution.largestAltitude(gain))