# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 10:52:04 2021
IDEXX_Results.py v1.1
Last updated Mar 29 2021
@author: kea5359
kea5359@psu.edu
kalbert15@su.edu
"""
import csv
import shutil
import os
import sys
import time


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

print('IDEXX_Results.py v1.1')
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
print('Ensure that ALL wells were selected when exporting PCR results')
for i in range(2):
    print('')


print('This program converts a text file (.txt) from the results of the qPCR run, exported from the 7500')
print('to a CSV file (.csv) containing the results, to be uploaded onto LIMS')

for i in range(2):
    print('')


print('Ensure the proper text file was put into the input folder within the 3_IDEXX_PCR_Results folder')
print(inputdir)

for i in range(1):
    print('')

print('The PCR results CSV file will be output into the output folder within the 3_IDEXX_PCR_Results folder')
print(outputdir)

for i in range(1):
    print('')

print('The text file selected from the input folder will be moved to the archive folder after the program is complete')
print('The contents that were in the output folder from previous program executions will also be moved to the archive folder')

for i in range(1):
    print('')

print('If the program fails to work, ensure the text file you would like to use is not present in both the input and archive folders')
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

resultstextfile = inputlist[filenumber]
qPCRbarcode = resultstextfile[0: len(resultstextfile) - 9]


PCRresults = open(inputdir + '\\' + resultstextfile, "r")
results = [(line.strip()).split() for line in PCRresults]
PCRresults.close()





"""
Class implementation for barcodes
"""
rows = ["A", "B", "C", "D", "E", "F", "G", "H"]
columns = ["1","2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
dictionary = []
for column in columns:
    for row in rows:
        dictionary.append(row + column)

class Barcodes():
    def __init__(self, qPCR_Barcode, Well_ID, Sample_Barcode, CT_SARS, CT_RP):
        self.qPCR_Barcode = qPCR_Barcode
        self.Well_ID = Well_ID
        self.Sample_Barcode = Sample_Barcode
        self.CT_SARS = CT_SARS
        self.CT_RP = CT_RP

results.remove(results[6])





"""
Generate a list of all the sample barcodes
"""
sample_barcodes = []
for i in range(len(results)):
    if len(results[i]) > 10:
        if results[i][0] in dictionary and results[i][1] not in sample_barcodes:
            sample_barcodes.append(results[i][1])





"""
Check that the whole plate was exported and not just one individual sample or
only controls
"""
if len(sample_barcodes) <= 4:
    print('Only ' + str(len(sample_barcodes)) + ' well(s) was/were selected when exporting the PCR results')
    print('Delete the exported textfile from the input folder')
    print('Please export the file from the 7500 software again, with ALL wells selected')
    exportstatus = 1

else:
    exportstatus = 0



if exportstatus == 1:
    for i in range(1):
        print('')
        
    exitscript = input('Would you like to close the script? (y/n)')
    while exitscript != "y" or exitscript != "n":
        if exitscript == "y":
            sys.exit()
        if exitscript == "n":
            break
        exitscript = input("Would you like to close the script? (y/n):")
        for i in range(3):
            print('')





"""
Get class implementation for the barcodes and associate the well id, PCR barcode,
and sample barcode together
"""
for i in range(len(sample_barcodes)):
    for j in range(len(results)):
        if len(results[j]) > 10:
            if sample_barcodes[i] == results[j][1]:
                sample_barcodes[i] = Barcodes(qPCRbarcode, results[j][0], sample_barcodes[i], "", "")






"""
Add the SARS and RP ct values associated with each sample_barcode
"""
for i in range(len(sample_barcodes)):
    for j in range(len(results)):
        if len(results[j]) >10:
            if sample_barcodes[i].Sample_Barcode == results[j][1] and sample_barcodes[i].Well_ID == results[j][0] and results[j][2] == "RP":
                sample_barcodes[i].CT_RP = results[j][6]
            if sample_barcodes[i].Sample_Barcode == results[j][1] and sample_barcodes[i].Well_ID == results[j][0] and results[j][2] == "SARS-CoV-2":
                sample_barcodes[i].CT_SARS = results[j][6]
         



    
"""
Remove the PEC NEC PAC NTC sample barcodes names so the LIMS upload is satisfied
"""
for i in range(len(sample_barcodes)):
    b = sample_barcodes[i]
    if b.Sample_Barcode == "NEC" or b.Sample_Barcode == "PEC" or b.Sample_Barcode == "PAC" or b.Sample_Barcode == "NTC":
        b.Sample_Barcode = ''





"""
Create LIMS Results csv
"""  
with open(qPCRbarcode + ' - LIMS Results.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['qPCR Plate Barcode', 'Well ID', 'Sample Barcode', 'Ct SARS', 'Ct RP'])
    for i in range(len(sample_barcodes)):
        b = sample_barcodes[i]
        writer.writerow([b.qPCR_Barcode, b.Well_ID, b.Sample_Barcode, b.CT_SARS, b.CT_RP])
f.close()


print('The CSV of the results file, ' + qPCRbarcode + ' - LIMS Results.csv, has been successfully created.')
for i in range(2):
    print('')





"""
Move files to output folders and archives
"""
for i in range(len(outputlist)):
    shutil.move(outputdir + "//" + outputlist[i], archivedir)

shutil.move(qPCRbarcode + ' - LIMS Results.csv', outputdir)
shutil.move(inputdir + "//" + resultstextfile, archivedir)

print('The CSV of the results is in the output folder and ready for upload to LIMS')

time.sleep(20)
