class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        tot = 0
        s = set()
        for i in answers:
            if i == 0:
                tot += 1
            else:
                if i not in s:
                    s.add(i)
                    temp = answers.count(i)
                    temp2 = i + 1
                    tot += (temp2*(math.ceil(temp/temp2)))

            
        return tot