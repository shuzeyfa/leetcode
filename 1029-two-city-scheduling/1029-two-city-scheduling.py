class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        dif = []
        for i,j in costs:
            dif.append(i-j)

        d={}

        for i,val in enumerate(dif):
            d[i]=val

        so = dict(sorted(d.items(), key=lambda item:item[1]))
        tot = 0
        n = len(costs)//2
        for i in so:
            if n>0:
                tot += costs[i][0]
                n -= 1
            else:
                tot += costs[i][1]

        return (tot)