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
PCRtxtfile =r"""* Block Type = 96fast
* Chemistry = TAQMAN
* Experiment File Name = C:\Applied Biosystems\7500\bin\Untitled
* Experiment Run End Time = Not Started
* Instrument Type = sds7500fast
* Passive Reference = ROX

[Sample Setup]
Well	Sample Name	Sample Color	Biogroup Name	Biogroup Color	Target Name	Target Color	Task	Reporter	Quencher	Quantity	Comments
A1	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
A1	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
A2	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
A2	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
A3	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
A3	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
A4	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
A4	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
A5	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
A5	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
A6	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
A6	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
A7	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
A7	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
A8	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
A8	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
A9	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
A9	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
A10	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
A10	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
A11	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
A11	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
A12	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
A12	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
B1	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
B1	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
B2	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
B2	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
B3	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
B3	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
B4	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
B4	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
B5	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
B5	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
B6	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
B6	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
B7	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
B7	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
B8	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
B8	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
B9	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
B9	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
B10	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
B10	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
B11	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
B11	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
B12	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
B12	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
C1	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
C1	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
C2	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
C2	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
C3	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
C3	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
C4	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
C4	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
C5	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
C5	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
C6	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
C6	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
C7	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
C7	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
C8	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
C8	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
C9	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
C9	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
C10	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
C10	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
C11	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
C11	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
C12	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
C12	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
D1	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
D1	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
D2	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
D2	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
D3	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
D3	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
D4	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
D4	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
D5	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
D5	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
D6	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
D6	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
D7	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
D7	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
D8	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
D8	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
D9	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
D9	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
D10	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
D10	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
D11	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
D11	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
D12	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
D12	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
E1	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
E1	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
E2	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
E2	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
E3	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
E3	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
E4	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
E4	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
E5	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
E5	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
E6	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
E6	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
E7	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
E7	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
E8	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
E8	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
E9	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
E9	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
E10	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
E10	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
E11	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
E11	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
E12	PEC	"RGB(132,193,241)"			RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
E12	PEC	"RGB(132,193,241)"			SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
F1	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
F1	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
F2	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
F2	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
F3	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
F3	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
F4	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
F4	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
F5	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
F5	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
F6	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
F6	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
F7	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
F7	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
F8	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
F8	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
F9	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
F9	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
F10	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
F10	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
F11	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
F11	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
F12	NEC	"RGB(168,255,222)"			RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
F12	NEC	"RGB(168,255,222)"			SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
G1	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
G1	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
G2	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
G2	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
G3	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
G3	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
G4	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
G4	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
G5	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
G5	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
G6	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
G6	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
G7	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
G7	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
G8	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
G8	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
G9	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
G9	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
G10	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
G10	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
G11	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
G11	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
G12	PAC	"RGB(223,221,142)"			RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
G12	PAC	"RGB(223,221,142)"			SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
H1	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
H1	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
H2	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
H2	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
H3	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
H3	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
H4	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
H4	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
H5	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
H5	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
H6	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
H6	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
H7	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
H7	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
H8	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
H8	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
H9	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
H9	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
H10	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
H10	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
H11	replace				RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
H11	replace				SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
H12	NTC	"RGB(247,255,168)"			RP	"RGB(208,243,98)"	UNKNOWN	VIC	None		
H12	NTC	"RGB(247,255,168)"			SARS-CoV-2	"RGB(139,189,249)"	UNKNOWN	FAM	None		
"""

list_of_lines = PCRtxtfile.splitlines()

for i in range(len(barcodes)):
    for j in range(len(list_of_lines)):
        number = list_of_lines[j][1:3]
        if number == "10" or number == "11" or number == "12":
            PCRwellid = list_of_lines[j][:3]
        else:
            PCRwellid = list_of_lines[j][:2]
    
        if PCRwellid == barcodes[i][0]['Well ID']:
            list_of_lines[j] = list_of_lines[j].replace('replace', barcodes[i][0]['Sample Barcode'])

removal_index = []
for i in range(len(list_of_lines)):
    if "replace" in list_of_lines[i]:
        removal_index.append(i)
removal_index.sort(reverse=True)

for index in removal_index:
    del list_of_lines[index]



with open(barcodes[1][0]['qPCR Plate Barcode'] + " - PCR template.txt", "w") as template:
    for line in list_of_lines:
            template.write(f"{line}\n")


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
