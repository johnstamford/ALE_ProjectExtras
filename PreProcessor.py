# ========================================
# Preprocessing the images for use
# in training the Neural Network
#
# Author: John Stamford
# ========================================

import os
import Image

class PreProcessor:

    folder = ""
    OutputString = ""
    def SetFolder(self, folder="./"):
        self.folder = folder
    
    def BmpToPng(self):
        print self.folder
        print "Converting to PNG"
        count = 0
        ls = os.listdir(self.folder)
        for f in ls:
            name, ext = os.path.splitext(f)
            
            if ext.lower() == ".bmp":
                outfile = name + ".png"
                #print '  ' + f + ' -> ' + outfile
                try:
                    Image.open(self.folder + f).save(self.folder + outfile)
                except IOError:
                    print "ERROR - Can not load image " + self.folder + f
                count += 1

                # Delete .bmp files
                try:
                    os.remove(self.folder + f)
                except IOError:
                    print "ERROR - Can not delete image " + self.folder + f  

        print "Converted " + str(count) + " Files"

    def ToString(self, img):
        self.OutputString = ""
        for pixel in iter(img.getdata()):
            self.OutputString += str(pixel) + ", "

            
            
        #print PixelString

    def Downsample(self,w=32,h=32, CSV=False):
        print "Converting to PNG"

        TextFile = self.folder + "data.txt"
        
        if CSV == True:
            print "CSV - Creating the file"
            f = open(TextFile, "w")
            f.truncate()
            
        count = 0
        ls = os.listdir(self.folder)
        for f in ls:
            name, ext = os.path.splitext(f)
            if ext.lower() == ".png":
                # Open the image
                img = Image.open(self.folder + f)
                # Convert to Grayscale
                img = img.convert('L')
                # Resize
                size = (w,h)
                img = img.resize(size, Image.ANTIALIAS)
                # Save
                img.save(self.folder + "thumbs/" + f)

                if CSV == True:
                    self.ToString(img)
                    with open(TextFile, "a") as myfile:
                        myfile.write(self.OutputString + "\n")

    
            
if __name__=='__main__':
    p = PreProcessor()
    p.SetFolder("../Msc/ALE4/gameplay/")
    p.BmpToPng()
    p.Downsample(32,32,True)
