class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kelvin=celsius+273.15
        fahr=(celsius*1.80)+32.00
        l=[]
        l.append(kelvin)
        l.append(fahr)
        
        return l