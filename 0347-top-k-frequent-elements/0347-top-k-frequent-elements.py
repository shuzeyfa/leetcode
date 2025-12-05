class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d=Counter(nums)
        ans= []
        
        sor = dict(sorted(d.items(),key=lambda item:item[1],reverse=True))
        ind=k
        for i in sor:
            if ind>0:
                ans.append(i)
                ind-=1
            else:
                break
        return ans