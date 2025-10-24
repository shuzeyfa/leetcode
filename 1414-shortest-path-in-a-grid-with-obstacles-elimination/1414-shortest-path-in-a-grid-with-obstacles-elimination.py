class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:

        n, m = len(grid), len(grid[0])

        heap = [(0, 0, 0, k)]
        visited = {(0, 0, 0)}
        
        while heap:
            val2, row, col, rem = heappop(heap)

            if row == len(grid) -1 and col == len(grid[0]) - 1:
                return val2
            
            
            t = False

            if row+1 < n:
                if grid[row+1][col] == 1:
                    if rem > 0:
                        t = True
                        if (row+1, col, rem-1) not in visited:
                            visited.add((row+1, col, rem-1))
                            heappush(heap, (val2+1, row+1, col, rem-1))
                        
                else:
                    if (row+1, col, rem) not in visited:
                        visited.add((row+1, col, rem))
                        heappush(heap, (val2+1, row+1, col, rem))

            if row-1 >= 0:
                if grid[row-1][col] == 1:
                    if rem > 0:
                        t = True
                        if (row-1, col, rem-1) not in visited:
                            visited.add((row-1, col, rem-1))
                            heappush(heap, (val2+1, row-1, col, rem-1))
                        
                else:
                    if (row-1, col, rem) not in visited:
                        visited.add((row-1, col, rem))
                        heappush(heap, (val2+1, row-1, col, rem))

            if col+1 < m:
                if grid[row][col+1] == 1:
                    if rem > 0:
                        t = True
                        if (row, col+1, rem-1) not in visited:
                            visited.add((row, col+1, rem-1))
                            heappush(heap, (val2+1, row, col+1, rem-1))
                        
                else:
                    if (row, col+1, rem) not in visited:
                        visited.add((row, col+1, rem))
                        heappush(heap, (val2+1, row, col+1, rem))

            if col-1 >= 0:
                if grid[row][col-1] == 1:
                    if rem > 0:
                        t = True
                        if (row, col-1, rem-1) not in visited:
                            visited.add((row, col-1, rem-1))
                            heappush(heap, (val2+1, row, col-1, rem-1))
                        
                else:
                    if (row, col-1, rem) not in visited:
                        visited.add((row, col-1, rem))
                        heappush(heap, (val2+1, row, col-1, rem))


        return -1

