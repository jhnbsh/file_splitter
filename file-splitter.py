#!/usr/bin/python

#Program: v1.0
#Description: This program splits extremly large files (tested up to 150GB) into smaller ones by the specified number of lines. 


#Requried modules.
import sys, io, codecs, chardet

#Take arguments from command line.
inputfile = sys.argv[1]
maxlines= int(sys.argv[2])

with open (inputfile) as input:
    #Create output file.
    output = codecs.open("output_0.txt", 'wb', encoding=('ascii'), errors=('ignore'))
    for i,line in enumerate(input):
        output.write(line)
        #Stop loop when maxlines has been reached (i+1 is a multiple of maxlines).
        if (i+1)%maxlines == 0:
        	#Close the current output file.
        	output.close()
        	#Open a new file with incremented file name.
        	output = codecs.open("output_%d.txt"%(i/maxlines+1),'wb', encoding=('ascii'), errors=('ignore'))
    output.close()