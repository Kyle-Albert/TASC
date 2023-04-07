# -*- coding: utf-8 -*-

import time
import csv
import os
import shutil
import sys

"""
Get directories and lists together for the files in the input, output, and 'root'
folders
"""
currentdir = os.getcwd()

inputdir = os.getcwd() + "\\Input"
inputlist = os.listdir(inputdir)

outputdir = os.getcwd() + "\\Output"
outputlist = os.listdir(outputdir)

archivedir = os.getcwd() + "\\Archive"
archivelist = os.listdir(archivedir)

print('IDEXX_PCR_Template.py v1.1')
print('')


"""
Detect duplicate files and hault script from progressing until the duplicates have been removed.
"""
duplicatefilecount = 0
for i in range(len(outputlist)):
    for j in range(len(archivelist)):
        if outputlist[i] == archivelist[j]:
            duplicatefilecount += 1
            print('"' + outputlist[i] + '" exists in both the archive and OUTPUT folders. The program will not proceed until "' + outputlist[i] + '" is removed from the archive folder' )
            for k in range(2):
                print("")

for i in range(len(inputlist)):
    for j in range(len(archivelist)):
        if inputlist[i] == archivelist[j]:
            duplicatefilecount += 1
            print('"' + inputlist[i] + '" exists in both the archive and INPUT folders. The program will not proceed until "' + inputlist[i] + '" is removed from the archive folder' )
            for k in range(2):
                print("")

if duplicatefilecount > 0:
    print("The program will close in 20 seconds. Please correct the duplicate files and execute the program again.")
    time.sleep(20)
    sys.exit()



"""
Print messages to the user to indicate how the script functions
"""


print('This program converts a CSV file (.csv) from \"Generate qPCR Run file\" downloaded from LIMS')
print('to a text file (.txt) containing the PCR template, to be uploaded onto the PCR\'s 7500 software')

for i in range(2):
    print('')


print('Ensure the proper CSV file was put into the input folder within the 2_IDEXX_PCR_Template_Generation folder')
print(inputdir)

print('')

print('The PCR template text file will be output into the output folder within the 2_IDEXX_PCR_Template_Generation folder')
print(outputdir)


print('')

print('The CSV file selected from the input folder will be moved to the archive folder after the program is complete')
print('The contents that were in the output folder from previous program executions will also be moved to the archive folder')

print('')

print('If the program fails to work, ensure the CSV file you would like to use is not present in both the input and archive folders')
print('Additonally, ensure there are not files present in the both the output and archive folders with the same name')
print('Do not run the same file twice as it will cause errors. It this occurs, delete the unwanted outputs from the archive and delete the')
print('resulting outputs, then run the proper file.')

for i in range(5):
    print('')






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

csvlims = inputlist[filenumber]





"""
Load in the CSV file from LIMS as the barcodes element
"""
barcodes = []
with open(inputdir + '\\' + csvlims) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        barcodes.append([row])




"""
Opens the PCR Template text file and updates it with the new
sample information. Saves this new textfile as the barcode name. 
To be uploaded to the machine
"""
PCRtxtfile = open("IDEXX PCR Template.txt", "r")
list_of_lines = PCRtxtfile.readlines()

for i in range(len(barcodes)):
    for j in range(len(list_of_lines)):
        number = list_of_lines[j][1:3]
        if number == "10" or number == "11" or number == "12":
            PCRwellid = list_of_lines[j][:3]
        else:
            PCRwellid = list_of_lines[j][:2]
    
        if PCRwellid == barcodes[i][0]['Well ID']:
            list_of_lines[j] = list_of_lines[j].replace('replace', barcodes[i][0]['Sample Barcode'])
            
for i in range(len(list_of_lines)):
    if "replace" in list_of_lines[i]:
        list_of_lines[i] = ''
      
PCRtxtfile = open(barcodes[1][0]['qPCR Plate Barcode'] + " - PCR template.txt", "w")
PCRtxtfile.writelines(list_of_lines)
PCRtxtfile.close()


print('The PCR Template, ' + barcodes[1][0]['qPCR Plate Barcode'] + ' - PCR template.txt, has been successfully created')
for i in range(2):
    print('')





"""
Move files to output folders and archives
"""
for i in range(len(outputlist)):
    shutil.move(outputdir + "//" + outputlist[i], archivedir)

shutil.move(barcodes[1][0]['qPCR Plate Barcode'] + " - PCR template.txt", outputdir)
shutil.move(inputdir + "//" + csvlims, archivedir)




print('The PCR template file is in the output folder and can be imported to the 7500 software')


time.sleep(20)
