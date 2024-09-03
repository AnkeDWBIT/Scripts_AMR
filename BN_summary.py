#!/usr/bin/env python
# Script that makes an Excel file to summarize the raw data results from running BioNumerics on the E. coli WGS

# Importing the required libraries
import os
import xlsxwriter

# In a folder, look for each subfolder and save the folder name as the sample name
input_dir = "/home/guest/BIT11_Traineeship/Ecoli_AMR/BioNumerics_out"

# List of antibiotics to look for in the ResFinder results
AB_list = ["amikacin", "amoxicillin", "amoxicillin+clavulanic acid", "aztreonam",
            "cefepime", "ceftazidime", "ciprofloxacin", "colistin", "meropenem", 
            "piperacillin", "piperacillin+tazobactam", "tigecycline", "tobramycin",
            "trimethoprim", "sulfamethoxazole"
            ]

# STEP 1 : Make an Excel file to store the summary data further in the script
####################################################################################################################################
output_file = "BN_summary.xlsx"
output_dir = "/home/guest/BIT11_Traineeship/Ecoli_AMR/Summary_Excel"
wb = xlsxwriter.Workbook(os.path.join(output_dir, output_file))
ws = wb.add_worksheet("BN_summary")

# Write the header line
header = ["File_ID"] + AB_list
ws.write_row(0, 0, header) 

# Initialize the Excel line counter
excel_line = 2

# STEP 2 : Retrieve antibiotic resistances from BioNumerics data
####################################################################################################################################
# Sort the subfolders to make sure the order is consistent
subdirs = sorted([d for d in os.listdir(input_dir) if os.path.isdir(os.path.join(input_dir, d))])

# Loop through each subfolder (=sample)
for subdir in subdirs:
    subdir_path = os.path.join(input_dir, subdir)
    for filename in os.listdir(subdir_path):
        sample = os.path.basename(subdir)

    # Make a list to store the phenotypic data
    pheno_data = [sample]

    # Make a list to store the antibiotic resistances foud in the sample
    AB_sample = []
   
    # Go through the output files per sample and search for the files with phenotypic data
    files = os.listdir(subdir_path)
    for file in files:

        if file == "Resistance-ResultsTableAcq.tsv":
            file_path = os.path.join(subdir_path, file)
            #print(f"Found data for sample {sample} in file {file_path}")
            
            # Read the file
            with open(file_path, 'r') as file:
                lines = file.readlines()
                # Iterate through the lines, skipping the first line
                for i, line in enumerate(lines):
                    if i == 0:
                        continue  # Skip the first line (header)
                    # Split the line into columns
                    parts = line.split('\t')
                    antibiotic = parts[0].strip().lower()
                    AB_sample.append(antibiotic)
       
        if file == "Resistance-ResultsTableMut.tsv":
            file_path = os.path.join(subdir_path, file) 
            # Read the file
            with open(file_path, 'r') as file:
                lines = file.readlines()
                # Iterate through the lines, skipping the first line
                for i, line in enumerate(lines):
                    if i == 0:
                        continue
                    # Split the line into columns
                    parts = line.split('\t')
                    antibiotic = parts[0].strip().lower()
                    AB_sample.append(antibiotic)

# STEP 3 : Fill in the Excel file with the phenotypic data for each AB in the study for each sample/strain
#####################################################################################################
    # Compare the ABs from the study with the ABs found in the sample
    for AB in AB_list:
        if AB.lower() in AB_sample:
            pheno_data.append("R")
        else:
            pheno_data.append("S")

    # Write the phenotypic data from the strain to the Excel file
    ws.write_row(excel_line, 0, pheno_data)
        
    # Add to the Excel line counter
    excel_line += 1
                
# Close the workbook
wb.close()                     
                        
# Print a message to indicate the script has finished
print("Summary Excel file has been created successfully!")
