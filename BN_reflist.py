#!/usr/bin/env python
# Script to go through the Bionumerics raw data of the E. coli WGS & create a reference list of all the genes found and their corresponding resistance phenotypes/antibiotics

# Importing the required libraries
import os
import xlsxwriter
import openpyxl

# Define the input-dir & output-file
input_dir = "/home/guest/BIT11_Traineeship/Ecoli_AMR/BN_data/"
output_file = "/home/guest/BIT11_Traineeship/Ecoli_AMR/BN_reflist.xlsx"

# STEP 1 : Retrieve data from the input_dir and save it in a dictionary
############################################################################################################################################################
# Loop through the input directory and look for the files named "Resistance_ResultsTableAcq.tsv"
data_dict = {}
for subdir, dirs, files in os.walk(input_dir):
    sample = os.path.basename(subdir)
    for file in files:
        if file == "Resistance-ResultsTableAcq.tsv":
            file_path = os.path.join(subdir, file)
            #print(f"Found data for sample {sample} in file {file}")
            # Read the text file
            with open(file_path, 'r') as file:
                lines = file.readlines()
                # Iterate through the lines, skipping the first line
                for i, line in enumerate(lines):
                    if i == 0:
                        continue  # Skip the first line (header)
                    # Split the line into columns
                    parts = line.split('\t')
                    gene = parts[1].strip()
                    antibiotic = parts[0].strip()
                    # Add the gene & antibiotict to the dictionary
                    if gene not in data_dict:
                        data_dict[gene] = [antibiotic]                      # If gene not present yet : add gene + AB    
                    else:
                        if antibiotic not in data_dict[gene]:               # If gene is present, but AB not : add AB to gene
                            data_dict[gene].append(antibiotic)
                        else:
                            continue                                        # If gene & AB are present : continue

#print(data_dict)
                        
# STEP 2 : Create an Excel file to store the reference list
############################################################################################################################################################
wb = xlsxwriter.Workbook(output_file)
ws = wb.add_worksheet("BN_reflist")
# Write the header line
header = ["Gene", "Antibiotic"]
ws.write_row(0, 0, header)

# Write the data to the Excel file
row = 2
for gene, AB_list in data_dict.items():
    ws.write(row, 0, gene)
    ws.write(row, 1, ", ".join(AB_list))
    row += 1

# Close the Excel file
wb.close()