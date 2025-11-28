class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        ans = set()
        q = deque([0])
        ans.add(0)

        while q:
            cur = q.popleft()
            
            for i in rooms[cur]:
                if i not in ans:
                    q.append(i)
                    ans.add(i)

        if len(ans) < len(rooms):
            return False
        return True