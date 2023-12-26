from dataclasses import dataclass

@dataclass
class RGBdata:
    RED: int
    GREEN: int
    BLUE: int
    BRIGHTNESS: int
    def __init__(self, red: int = 0, green: int = 0, blue: int = 0, brightness: int = 100):
        self.RED = red
        self.BLUE = blue
        self.GREEN = green
        self.BRIGHTNESS = brightness

    def output_bytes(self) -> bytes:
        if self.BRIGHTNESS >= 100:
            self.BRIGHTNESS = 100

        # Calculate RGB values with brightness adjustment
        red_value = int(self.RED * self.BRIGHTNESS/100 )
        green_value = int(self.GREEN * self.BRIGHTNESS/100)
        blue_value = int(self.BLUE * self.BRIGHTNESS/100)

        # Pack RGB values into a 3-byte representation (bytes)
        output = bytes([green_value, red_value, blue_value])
        return output

    def outputInt(self):
        output = 0
        if self.BRIGHTNESS >= 100:
            self.BRIGHTNESS = 100
        output = (int(self.GREEN / self.BRIGHTNESS) << 16) | (int(self.RED/ self.BRIGHTNESS)  << 8) | int(self.BLUE/ self.BRIGHTNESS) 
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

    def ws2812_SPI(self, led: int = 0):
        color = self.pixels[led].output_bytes()
        outputArray=[0]*24
        index = 0
        for i in range(23, -1, -1):
            if ((color >> i) & 0x01) == 1:
                outputArray[index] = 0b110  # store 1
            else:
                outputArray[index] = 0b100  # store 0
            index += 1
        return outputArray