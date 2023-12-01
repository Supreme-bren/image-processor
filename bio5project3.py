import bmp

class ImageProcessor:
    def __init__(self,filename):#Initilizer
        self.pixelgrid = bmp.ReadBMP(filename) #stores a 3d grd of pixelgrid
        self.height = len(self.pixelgrid)
        self.width = len(self.pixelgrid[0])

    def save(self,newName):
        bmp.WriteBMP(self.pixelgrid,newName)

    def invert(self):
        for row in range(self.height):
            for pixel in range(self.width):
                for channel in range(3):
                    self.pixelgrid[row][pixel][channel] = 255-self.pixelgrid[row][pixel][channel]

    def displayChannel(self,channel):
        if channel=='r':
            for row in range(self.height):
                for pixel in range(self.width):
                    self.pixelgrid[row][pixel][1]-=self.pixelgrid[row][pixel][1]
                    self.pixelgrid[row][pixel][2]-=self.pixelgrid[row][pixel][2]
        elif channel=='g':
            for row in range(self.height):
                for pixel in range(self.width):
                    self.pixelgrid[row][pixel][0]-=self.pixelgrid[row][pixel][0]
                    self.pixelgrid[row][pixel][2]-=self.pixelgrid[row][pixel][2]
        elif channel=='b':
            for row in range(self.height):
                for pixel in range(self.width):
                    self.pixelgrid[row][pixel][0]-=self.pixelgrid[row][pixel][0]
                    self.pixelgrid[row][pixel][1]-=self.pixelgrid[row][pixel][1]
    def flip(self,axis):
        if axis=='h':
            self.pixelgrid.reverse()
        elif axis=='v':
            for row in range(self.height):
                    self.pixelgrid[row].reverse()
    def grayscale(self):
        for row in range(self.height):
                for pixel in range(self.width):
                    gray=(self.pixelgrid[row][pixel][0]+self.pixelgrid[row][pixel][1]+self.pixelgrid[row][pixel][2])//3
                    self.pixelgrid[row][pixel][0]=gray
                    self.pixelgrid[row][pixel][1]=gray
                    self.pixelgrid[row][pixel][2]=gray
    def brightness(self,operation):
        if operation=='+':
            for row in range(self.height):
                for pixel in range(self.width):
                    adjustR=self.pixelgrid[row][pixel][0]+25
                    if adjustR>255:
                        adjustR=255
                    adjustG=self.pixelgrid[row][pixel][1]+25
                    if adjustG>255:
                        adjustG=255
                    adjustB=self.pixelgrid[row][pixel][2]+25
                    if adjustB>255:
                        adjustB=255

                    self.pixelgrid[row][pixel][0]=adjustR
                    self.pixelgrid[row][pixel][1]=adjustG
                    self.pixelgrid[row][pixel][2]=adjustB
        elif operation=='-':
            for row in range(self.height):
                for pixel in range(self.width):
                    adjustR=self.pixelgrid[row][pixel][0]-25
                    if adjustR<0:
                        adjustR=0
                    adjustG=self.pixelgrid[row][pixel][1]-25
                    if adjustG<0:
                        adjustG=0
                    adjustB=self.pixelgrid[row][pixel][2]-25
                    if adjustB<0:
                        adjustB=0

                    self.pixelgrid[row][pixel][0]=adjustR
                    self.pixelgrid[row][pixel][1]=adjustG
                    self.pixelgrid[row][pixel][2]=adjustB
    def contrast(self):
        choice=0
        while choice!='q':
            choice=input("Enter (+) to increase contrast,(-) to decrease contrast,(q) to quit: ")
            print("DONE")
            if choice=='+':
                C=45
                factor=(259*(C+255))/(255*(259-C))
                for row in range(self.height):
                    for pixel in range(self.width):
                        for channel in range(3):
                            new_value=int(factor*(self.pixelgrid[row][pixel][channel]-128)+128)
                            if new_value>255:
                                new_value=255
                            if new_value < 0:
                                new_value=0
                            self.pixelgrid[row][pixel][channel]=new_value
            elif choice=='-':
                C=-45
                factor=(259*(C+255))/(255*(259-C))
                for row in range(self.height):
                    for pixel in range(self.width):
                        for channel in range(3):
                            new_value=int(factor*(self.pixelgrid[row][pixel][channel]-128)+128)
                            if new_value<0:
                                new_value=0
                            if new_value>255:
                                new_value=255
                            self.pixelgrid[row][pixel][channel]=new_value
            else:
                continue
def main():
    imgFile = input("Enter filename containing source image(must be.bmp): ")
    myPicture = ImageProcessor(imgFile)
    selection=0
    while selection!='q':
        print('='*30)
        print("Python Image Processor")
        print('='*30)
        menu="""
        a) Invert Colors
        b) Flip Image
        c) Display Color Channel
        d) Convert to Grayscale
        e) Adjust Brightness
        f) Adjust Contrast
        s) SAVE current image
        ----------------------
        o) Open New Image
        q) Quit
        """
        print(menu)
        print('='*30)
        selection=input("(a/b/c/d/e/f/q): ")

        if selection=='a':
            myPicture.invert()
            print("DONE!")
        elif selection=='b':
            axis=input("Please enter desired axis (h) or (v): ")
            myPicture.flip(axis)
            print("DONE")
        elif selection=='c':
            channel=input("Please select a channel to be displayed (r),(g), or(b): ")
            myPicture.displayChannel(channel)
            print("DONE")
        elif selection=='d':
            myPicture.grayscale()
            print("DONE")
        elif selection=='e':
            operation = input("Please enter (+) to increase, (-) deacrease, (q) to quit: ")
            while operation!='q':
                myPicture.brightness(operation)
                print("DONE")
                operation = input("Please enter (+) to increase, (-) to decrease, (q) to quit: ")
        elif selection=='f':
            myPicture.contrast()
        elif selection=='s':
            newFilename = input("Enter name of edited picture(must have .bmp extension): ")
            myPicture.save(newFilename)
            print("DONE")
        elif selection=='o':
            newImage = input("Please enter a new filename containing source image (must be .bmp): ")
            myPicture = ImageProcessor(newImage)
            print("DONE")


main()
