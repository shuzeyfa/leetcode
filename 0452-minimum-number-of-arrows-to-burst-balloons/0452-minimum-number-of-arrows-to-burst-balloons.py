class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda item:item[1])

        final = points[0][1]
        count = 1

        for start,end in points:
            if final < start:
                count += 1
                final = end

        return count
