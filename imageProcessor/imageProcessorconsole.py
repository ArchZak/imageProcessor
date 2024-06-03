import bmp 

class Imageprocessor:

    def __init__(self, filename):
        self.pixelgrid = bmp.ReadBMP(filename)
        self.height = len(self.pixelgrid)
        self.width = len(self.pixelgrid[0])        

    def save(self, newName):
        bmp.WriteBMP(self.pixelgrid, newName)

    def invert(self):
        for row in range(self.height):
            for column in range(self.width):
                for channel in range(3):
                    currentvalue = self.pixelgrid[row][column][channel]
                    newvalue = int(255-currentvalue)
                    self.pixelgrid[row][column][channel] = newvalue
    
    def displaychannel(self, channel):
        if channel == "r":  
            for row in range(self.height):
                for column in range(self.width):
                    for channel in range(3):
                        self.pixelgrid[row-1][column-1][0] 
                        self.pixelgrid[row][column][1] = 0
                        self.pixelgrid[row][column][2] = 0
        if channel == "g":  
            for row in range(self.height):
                for column in range(self.width):
                    for channel in range(3):
                        self.pixelgrid[row-1][column-1][0] = 0
                        self.pixelgrid[row][column][1]
                        self.pixelgrid[row][column][2] = 0
        if channel == "b":  
            for row in range(self.height):
                for column in range(self.width):
                    for channel in range(3):
                        self.pixelgrid[row-1][column-1][0] = 0
                        self.pixelgrid[row][column][1] = 0
                        self.pixelgrid[row][column][2] 
    
    def flip(self, axis):
        if axis == 'h':
            for row in range(self.height):
                self.pixelgrid[row].reverse()                   
        if axis == 'v':
            self.pixelgrid.reverse()
                        
    def grayscale(self):
        for row in range(self.height):
            for column in range(self.width):
                red = self.pixelgrid[row][column][0]
                green = self.pixelgrid[row][column][1]
                blue = self.pixelgrid[row][column][2]
                gray = (red + green + blue)//3
                self.pixelgrid[row][column][0] = gray
                self.pixelgrid[row][column][1] = gray
                self.pixelgrid[row][column][2] = gray

    def brightness(self, operation):
        if operation == '+':
            B = 25
        elif operation == '-':
            B = -25
        for row in range(self.height):
            for column in range(self.width):
                for channel in range(3):
                    currentvalue = self.pixelgrid[row][column][channel]
                    newvalue = int(currentvalue + B)
                    if newvalue > 255:
                        newvalue = 255
                    elif newvalue < 0:
                        newvalue = 0
                    self.pixelgrid[row][column][channel] = newvalue
    
    def contrast(self, operation):
        if operation == '+':
            C = 45
        elif operation == '-':
            C = -45
        factor = (259*(C+255))/(255*(259-C))
        for row in range(self.height):
            for column in range(self.width):
                for channel in range(3):
                    currentvalue = self.pixelgrid[row][column][channel]
                    newvalue = int(factor*(currentvalue-128)+128) 
                    if newvalue > 255:
                        newvalue = 255
                    elif newvalue < 0:
                        newvalue = 0
                    self.pixelgrid[row][column][channel] = newvalue
        
    
def main(): 
    filename = input("Enter filename containing source image (must be .bmp): ")
    processor = Imageprocessor(filename)
    while True:
        print("==============================\nPython Basic Image Processor\n==============================",
              "\nSelect an operation: \na) Invert Colors",
              "\nb) Flip Image\nc) Display color channel\nd) Convert to grayscale\ne) Adjust brightness\nf) Adjust contrast",
              "\ns) SAVE current image\n-------------------------\no) Open new image\nq) quit")
        operate = input("==============================\n(a/b/c/d/e/f/q): ")
        if operate == 'a':
            processor.invert()
        elif operate == 'b':
            axis = input("[v] flip photo vertically\n[h] flip photo horizontally\n[q] exit\n(v/h/q): ")
            if axis == "q":
                break
            else:
                processor.flip(axis)
        elif operate == 'c':
            channel = input("[r] display color channel to red\n[g] display color channel to green"+
                            "\n[b] display color channel to blue\n[q] exit\n(r/g/b/q): ")
            if channel == "q":
                break
            else:
                processor.displaychannel(channel)
        elif operate == 'd':
            processor.grayscale()
        elif operate == 'e':
            while True:
                operation = input("[+] increase brightness\n[-] decrease brightness\n[q] exit\n(+/-/q): ")
                if operation == 'q':
                    break
                else:
                    processor.brightness(operation)
        elif operate == 'f':
            while True:
                operation = input("[+] increase contrast\n[-] decrease contrast\n[q] exit\n(+/-/q): ")
                if operation == 'q':
                        break
                else:
                    processor.contrast(operation)
        elif operate == 's':
            newName = input("Enter name for edited picture (must have .bmp extension): ")
            processor.save(newName)
        elif operate == 'o':
            main()
        elif operate == 'q':
            break
main()