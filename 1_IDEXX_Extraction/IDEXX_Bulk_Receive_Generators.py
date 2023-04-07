# -*- coding: utf-8 -*-

import os
import sys
import csv
import shutil

currentdir = os.getcwd()
currentlist = os.listdir(currentdir)

inputdir = os.getcwd() + "\\Input"
inputlist = os.listdir(inputdir)

outputdir = os.getcwd() + "\\Output"
outputlist = os.listdir(outputdir)

archivedir = os.getcwd() + "\\Archive"

"""
Select the file you want to use
"""
numberdir = []
for i in range(len(inputlist)):
    print(str(i) + " : "  + inputlist[i])
    numberdir.append(str(i))
filenumber = input("Please input the number associated with the file:")

while filenumber not in numberdir:
    for i in range(6):
        print('')

    for i in range(len(inputlist)):
        print(str(i) + " : "  + inputlist[i])
    filenumber = input("Please input the number associated with the file:")
    
filenumber = int(filenumber)

textfile = inputlist[filenumber]
extractionbarcode = textfile[0 : len(textfile) - 4]

barcodetxtfile = open(inputdir + "//" + textfile, "r")#reads the barcode scans file from the desired date
barcodes = [(line.strip()).split() for line in barcodetxtfile]#makes each column of the file (each barcode) an element in a list
barcodetxtfile.close()#closes the file

barcode_len = len(barcodes)#determines how many barcodes are in the list

"""
Duplicate barcode check
"""
duplicatebarcodes = []
for i in range(barcode_len):
    jindex = []
    for j in range(barcode_len):
        if barcodes[i] == barcodes[j] and i < j:
            jindex.append(str(j + 1))
        if j == barcode_len - 1 and jindex != [] and (barcodes[i] not in duplicatebarcodes):
            duplicatebarcodes.append(barcodes[i])
            print(str(str(barcodes[i])[2:len(str(barcodes[i]))-2]) + " has duplicates at positions " + str(i + 1) + ", " + ", ".join(jindex))

if duplicatebarcodes != []:
    print("Duplicate barcodes detected")
    exitscript = input("Would you like to continue? (y/n):")
    while exitscript != "y" or exitscript != "n":
        if exitscript == "y":
            break
        if exitscript == "n":
            sys.exit()
        exitscript = input("Would you like to continue? (y/n):")
else:
    print("No duplicate barcodes")





"""
Delete Blank spaces entered in the textfile
Recreate the barcode_len variable with updated length
"""
deletenum = 0
for i in range(barcode_len):
    if len(barcodes[i]) == 0:
        barcodes[i] = ''
        deletenum += 1
        
for i in range(deletenum):
    barcodes.remove('')

barcode_len = len(barcodes)




"""
CSV Bulk receive
"""
with open(extractionbarcode + ' Bulk Receive CSV.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Sample Barcode', 'Record Type Id'])
    for i in range(barcode_len):
        writer.writerow([barcodes[i][0],'0124x000000dQUJ'])
f.close()

shutil.move(extractionbarcode + ' Bulk Receive CSV.csv', outputdir)

