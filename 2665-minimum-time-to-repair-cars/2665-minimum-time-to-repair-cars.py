class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def check(val):
            tot = 0
            for i in ranks:
                car =int(sqrt(val/i)) 
                tot += car
                if tot >= cars:
                    return True
            return False
        
        low = 1
        minn = min(ranks)
        high = minn*cars*cars

        while low<=high:
            mid = (low+ high) // 2
            if check(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans