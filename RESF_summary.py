#!/usr/bin/env python
# Script that makes an Excel file to summarize the raw data results from running ResFinder on the E. coli WGS

# Importing the required libraries
import os
import xlsxwriter

# In a folder, look for each subfolder and save the folder name as the sample name
input_dir = "/home/guest/BIT11_Traineeship/Ecoli_AMR/ResFinder_tool/resfinder_output"
data_file = "pheno_table.txt"

# List of antibiotics to look for in the ResFinder results
AB_list = ["amikacin", "amoxicillin", "amoxicillin+clavulanic acid", "aztreonam",
            "cefepime", "ceftazidime", "ciprofloxacin", "colistin", "meropenem", 
            "piperacillin", "piperacillin+tazobactam", "tigecycline", "tobramycin",
            "trimethoprim", "sulfamethoxazole"
            ]

# Make an Excel file to store the summary data
output_file = "ResFinder_summary.xlsx"
output_dir = "/home/guest/BIT11_Traineeship/Ecoli_AMR/ResFinder_tool/"
wb = xlsxwriter.Workbook(os.path.join(output_dir, output_file))
ws = wb.add_worksheet("ResFinder_summary")
# Write the header line
header = ["File_ID"] + AB_list
ws.write_row(0, 0, header) 

excel_line = 2
# Look in the input directory (ResFinder results) for subfolders (samples/strains)
pheno_data = []
sample_names = []
for subdir in os.listdir(input_dir):
    subdir_path = os.path.join(input_dir, subdir)
    if os.path.isdir(subdir_path):
        # Look through all the files and search the .txt files with the phenotypic data
        for filename in os.listdir(subdir_path):
            if filename == data_file:
                file_path = os.path.join(subdir_path, filename)
                #print(f"Found phenotypic data for sample {subdir} in file {filename}")

                 # Make a list to store the phenotypic data
                pheno_data = [subdir]

                # Read the text file and extract information
                with open(file_path, 'r') as file:
                    lines = file.readlines()
                    # Iterate through the lines
                    for AB in AB_list:
                        for line in lines:
                            # Split the line into columns
                            parts = line.split('\t')
                            if len(parts) >= 4:
                                antibiotic = parts[0].strip()
                                phenotype = parts[2].strip()
                                # If  a line contains the antibiotic of interest, extract the resistance phenotype
                                if AB == antibiotic:
                                    if parts[2].strip() == "No resistance":
                                        pheno_data.append("S")
                                    if parts[2].strip() == "Resistant":
                                        pheno_data.append("R")
                

                    # Write the phenotypic data from the strain to the Excel file
                    ws.write_row(excel_line, 0, pheno_data)

                    # Add to the Excel line counter
                    excel_line += 1
                    
                # Close the file
                file.close()

# Close the workbook
wb.close()                            
                        

