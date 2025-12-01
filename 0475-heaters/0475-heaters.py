class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:

        heaters.sort()
        ans = 0
        for house in houses:
            ind = bisect.bisect_left(heaters,house)
            if ind == 0:
                near = heaters[ind] - house
            elif ind == len(heaters):
                near = house - heaters[-1]
            else:
                near = min(house - heaters[ind-1],heaters[ind] - house)
            ans = max(ans, near)
        return ans