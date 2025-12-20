class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        if maxDoubles == 0 or target == 1:
            return target-1

        tot = 0
        while maxDoubles>0 and target>1:
            if target%2 == 1:
                tot += 2
            else:
                tot += 1
            target = target//2

            maxDoubles -= 1

        if target > 0:
            tot += (target - 1)
        return tot