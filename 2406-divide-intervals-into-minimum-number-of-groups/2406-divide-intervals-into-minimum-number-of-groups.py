class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        events=[]
        for i in intervals:
            events.append((i[0],1))
            events.append((i[1]+1,-1))
        events.sort(key=lambda x:(x[0],x[1]))
        c=0
        ma=0
        for event in events:
            c+=event[1]
            ma=max(ma,c)
        return ma            