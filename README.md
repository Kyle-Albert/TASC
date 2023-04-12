# TASC
These scripts function to help track the information about samples as they move through the lab. Starting with the extraction process, creating a plate map and upload the well ID of each sample to our Laboratory Information Management System (LIMS), prepare PCR templates for 7500 software, and convert PCR results to upload to LIMS.

## How to use
The basic function of each script is to take an input and produce an output. These scripts are designed for non-techincal users/users of any computer literacy level. A user will put a file into an "Input" folder, launch the script (on Windows this can be done by double-clicking script.py), and select which files to process. Processed files are in the "Output" folder.

Files which were previously in the "Output" folder are moved to the "Archive" folder. Files processed from "Input" are moved to "Archive" as well.

### 1_IDEXX_Extraction/IDEXX_Extraction_Scan.py
This script inputs a textfile, where the name of the textfile is the barcode for the extraction plate (sample_barcode.txt), and where each line of the text file contains a sample barcode (following wells A1=1, B1=2,..., A2=9, B2=10,..., D12=92).

There are 2 outputs:
+ csv containing the well ID for each sample as well as the barcode for the extraction plate to be uploaded to LIMS
+ An excel sheet with a visual plate map will be populated and automatically print (using default settings)

In our lab, we had barcode scanners programmed to "Enter" to a new line automatically. So a user would open Notepad on windows, scan the barcodes in, and save the file. This script will check for duplicate barcodes and also will remove whitespace after sample barcodes to ensure no errors occur.

IDEXX_Plate_Map.py will just generate a platemap to print out, instead of generating both a csv and platemap.

### 2_IDEXX_PCR_Template_Generation/IDEXX_PCR_Template.py
This script inputs a csv file downloaded from LIMS containing the sample barcodes, with their well ID, and the PCR plate barcode.

This script outputs a textfile of the PCR template to uploaded onto the 7500 software.

### 3_IDEXX_PCR_Results/IDEXX_Results.py
This script inputs a textfile containing the exported results of a PCR run.

This script outputs a csv file to be uploaded to LIMS containing each samples and controls RP and SARS Ct values.
