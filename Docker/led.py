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

    # def outputInt(self):
    #     output = 0
    #     if self.BRIGHTNESS >= 100:
    #         self.BRIGHTNESS = 100
    #     output = (int(self.GREEN / self.BRIGHTNESS) << 16) | (int(self.RED/ self.BRIGHTNESS)  << 8) | int(self.BLUE/ self.BRIGHTNESS) 
    #     return output
    
@dataclass
class Neopixel:
    
    def __init__(self, count: int =0):
        self.pixels = [RGBdata()] * count
        
    pixels = []
    
    # def outputData(self):
    #     outputArray = [int] * len(self.pixels) *3
    #     for i in range(len(self.pixels)):
    #         step = i *3
    #         outputArray[step] = self.pixels[i].GREEN
    #         outputArray[step+1] = self.pixels[i].RED
    #         outputArray[step+2] = self.pixels[i].BLUE
    #     return outputArray
    def set_pixel(self,pixel: int = 0 ,red: int = 0, green: int = 0, blue: int = 0, brightness: int =101):
        if brightness <= 100: 
            self.pixels[pixel].BRIGHTNESS = brightness
        self.pixels[pixel].RED = red
        self.pixels[pixel].GREEN = green
        self.pixels[pixel].BLUE = blue
        return 0

    def fill(self, red: int = 0, green: int = 0, blue: int = 0, brightness: int =101):
        for pixel in self.pixels:
            if brightness <= 100: 
                pixel.BRIGHTNESS = brightness
            pixel.RED = red
            pixel.GREEN = green
            pixel.BLUE = blue
        return 0

    def ws2812_Data(self):
        outputArray = [0] * (len(self.pixels) * 24)
        index = 0

        for pixel in self.pixels:
            color = pixel.output_bytes()

            for i in range(23, -1, -1):
                byte_index = i // 8
                bit_index = 7 - (i % 8)

                if ((color[byte_index] >> bit_index) & 0x01) == 1:
                    outputArray[index] = 0b11111100  # store 1
                else:
                    outputArray[index] = 0b10000000 # store 0
                index += 1

        return outputArray