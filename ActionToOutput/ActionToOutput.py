# ========================================
# Preprocessing the Actions for use
# in training the Neural Network
#
# Author: John Stamford
# ========================================

import os
import Image

class ActionToOutput:

    def __init__(self, file):
        print "Opening " + file
        try:
            f = open(file)
        except ValueError:
            print "ERROR"

        line = f.readline()
        line = line.rstrip('\n')

        #print "STARTING WITH " + self.GetOutput(line) + line

        count = 1

        # Open the output file
        print "Opening the Output File"
        try:
            s = open("Output.txt", "w")
        except ValueError:
            print "ERROR"
        
        while line:
            #print str(count) + " - Line: " + self.GetOutput(line)
            s.write(self.GetOutput(line) + "\n")
            count += 1
            line = f.readline()
            line = line.rstrip('\n')

        f.close()
        s.close()
        print "DONE"

    def GetOutput(self,s):
        action = "NA";
        if s == "0":
            action = "1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0"
        elif s == "1":
            action = "0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0"
        elif s == "2":
            action = "0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0"
        elif s == "3":
            action = "0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0"
        elif s == "4":
            action = "0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0"
        elif s == "5":
            action = "0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0"
        elif s == "6":
            action = "0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0"
        elif s == "7":
            action = "0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0"
        elif s == "8":
            action = "0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0"
        elif s == "9":
            action = "0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0"
        elif s == "10":
            action = "0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0"
        elif s == "11":
            action = "0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0"
        elif s == "12":
            action = "0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0"
        elif s == "13":
            action = "0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0"
        elif s == "14":
            action = "0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0"
        elif s == "15":
            action = "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0"
        elif s == "16":
            action = "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0"
        elif s == "17":
            action = "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1"
            
        return action
            
if __name__=='__main__':
    p = ActionToOutput("Controls.txt")

