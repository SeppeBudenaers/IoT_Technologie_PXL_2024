from dataclasses import dataclass

@dataclass
class RGBdata:
    RED: int
    GREEN: int
    BLUE: int

    def __init__(self, red:int = 0, green:int = 0 ,blue:int = 0):
        self.RED = red
        self.BLUE = blue
        self.GREEN = green
    
    def outputInt(self):
        output = 0
        output = (self.GREEN << 16) + (self.RED << 8) + self.BLUE
        return output
    
@dataclass
class Neopixel:
    
    def __init__(self, count: int =0):
        self.pixels = [RGBdata()] * count
        
    pixels = []
    
    def outputData(self):
        outputArray = [int] * len(self.pixels) *3
        for i in range(len(self.pixels)):
            step = i *3
            outputArray[step] = self.pixels[i].GREEN
            outputArray[step+1] = self.pixels[i].RED
            outputArray[step+2] = self.pixels[i].BLUE
        return outputArray