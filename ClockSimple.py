import math
from LedStrip import LedStrip



class ClockSimple():

    Letters = "KLOKKENVEROFEMTYVESKAMOJEKVARTATQTIAMINUTTERVEMOVERILPMMONALISHALVETTOTREFIREFEMSEKSRSYVOTTERNIMETIELLEVEATOLV"

    def __init__(self):
        self.ledStrip = LedStrip();

    hours = [
       [ 66, 67, ],
       [ 68, 69 ],
       [ 70, 71, 72 ],
       [ 73, 74, 75, 76 ],
       [ 77, 78, 79, ],
       [ 80, 81, 82, 83, ],
       [ 85, 86, 87 ],
       [ 88, 89, 90, 91 ],
       [ 93, 94 ],
       [ 97, 98, ],
       [ 99, 100, 101, 102, 103, 104 ],
       [ 106, 107, 108, 109]
    ]
    
    def turn_all_off(self):
        self.ledStrip.turn_all_off()

    def UpdateClock(self, hour, minute):
        self.ledStrip.ManipulateLeds(self.GetIndices(hour,minute))

    @staticmethod
    def RoundMinutes(minutes):
        return math.floor((minutes / 5)) * 5;
     

    def ThisHour(self, hour):
        if hour % 12 == 0 :
            return self.hours[12 - 1] 
        else:
            return self.hours[hour % 12 - 1]
      
    def NextHour(self,time):
        return self.ThisHour(time + 1);

    def GetIndices(self, hours, minutes):
        min = self.RoundMinutes(minutes = minutes)
        
        if min == 0:
            return [ 0, 1, 2, 3, 4, 5, 6, 8, 9 ]+self.ThisHour(hours)

        if min == 5: 
            return [ 0, 1, 2, 3, 4, 5, 6, 8, 9, 11, 12, 13, 36, 37, 38, 39, 40, 41, 42, 43, 47, 48, 49, 50 ]+self.ThisHour(hours)

        if min ==10: 
            return [ 0, 1, 2, 3, 4, 5, 6, 8, 9, 33, 34, 36, 37, 38, 39, 40, 41, 42, 43, 47, 48, 49, 50 ]+self.ThisHour(hours)

        if min ==15: 
            return [ 0, 1, 2, 3, 4, 5, 6, 8, 9, 25, 26, 27, 28, 29, 47, 48, 49, 50 ]+self.ThisHour(hours)

        if min ==20: 
            return [ 0, 1, 2, 3, 4, 5, 6, 8, 9, 14, 15, 16, 17, 36, 37, 38, 39, 40, 41, 42, 43, 47, 48, 49, 50]+self.ThisHour(hours)

        if min ==25: 
            return [ 0, 1, 2, 3, 4, 5, 6, 8, 9, 11, 12, 13, 36, 37, 38, 39, 40, 41, 42, 43, 51, 62, 63, 64, 65 ]+self.NextHour(hours)

        if min ==30: 
            return [ 0, 1, 2, 3, 4, 5, 6, 8, 9, 62, 63, 64, 65 ]+self.NextHour(hours)

        if min ==35: 
            return [ 0, 1, 2, 3, 4, 5, 6, 8, 9, 11, 12, 13, 36, 37, 38, 39, 40, 41, 42, 43, 47, 48, 49, 50, 62, 63, 64, 65 ]+self.NextHour(hours)

        if min ==40: 
            return [ 0, 1, 2, 3, 4, 5, 6, 8, 9, 14, 15, 16, 17, 36, 37, 38, 39, 40, 41, 42, 43, 51]+self.NextHour(hours)

        if min ==45: 
            return [ 0, 1, 2, 3, 4, 5, 6, 8, 9, 25, 26, 27, 28, 29, 51 ]+self.NextHour(hours)

        if min ==50: 
            return [ 0, 1, 2, 3, 4, 5, 6, 8, 9, 33, 34, 36, 37, 38, 39, 40, 41, 42, 43, 51]+self.NextHour(hours)

        if min ==55:    
            return [ 0, 1, 2, 3, 4, 5, 6, 8, 9, 11, 12, 13, 36, 37, 38, 39, 40, 41, 42, 43, 51 ]+self.NextHour(hours)