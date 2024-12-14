class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        angle_small=(hour%12)*30+minutes*0.5
        angle_large=minutes*6
        res1=abs(angle_large-angle_small)
        res2=360-res1
        return min(res1,res2)