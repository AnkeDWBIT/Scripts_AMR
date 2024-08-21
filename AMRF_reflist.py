#!/usr/bin/env python
# Script to go through the AMRFinder+ raw data of the E. coli WGS & create a reference list of all the genes found and their corresponding resistance phenotypes/antibiotics

# Importing the required libraries
import os
import xlsxwriter
import openpyxl
import csv

# Define the input-dir & output-file
input_dir = "/home/guest/BIT11_Traineeship/Ecoli_AMR/AMR_output/"
output_file = "/home/guest/BIT11_Traineeship/Ecoli_AMR/Reference_lists/AMRF_reflist.xlsx"

# STEP 1 : Retrieve data from the input_dir and save it in a dictionary
############################################################################################################################################################

data_dict = {}

# Loop through the input directory and look for the .tsv-files
files =  os.listdir(input_dir)
for file in files:
    if file.endswith(".tsv"):

       # Open .tsv-files with raw data
        file_path = os.path.join(input_dir, file)
        with open(file_path) as file_to_read:
            next(file_to_read) # Skip the header line when reading the file
            tsv_file = csv.reader(file_to_read, delimiter="\t")

            # Go through each line of data
            for line in tsv_file:
                # Save the gene names and associated antibiotics in the dictionary
                gene = line[5]
                # Alternatively shorten the gene name by removing the extension
                gene_short = gene.split("_")[0]
                antibiotics = line[11].lower().split("/")
                #print(file, gene, gene_short, antibiotic)

                # Fill the dictionary with the gene names and associated antibiotics
                if gene_short not in data_dict:
                    data_dict[gene_short] = antibiotics                     # If gene not present yet : add gene + AB    
                else:
                    for antibiotics in antibiotics:
                        if antibiotics not in data_dict[gene_short]:
                            data_dict[gene_short].append(antibiotics)
                        else:   
                            continue                                        # If gene & AB are present


# STEP 2 : Create an Excel file to store the reference list
############################################################################################################################################################
wb = xlsxwriter.Workbook(output_file)
ws = wb.add_worksheet("AMRF_reflist")
# Write the header line
header = ["Gene", "Antibiotic"]
ws.write_row(0, 0, header)

# Write the data to the Excel file
row = 2
for gene_short, AB_list in data_dict.items():
    AB_set = set(AB_list)
    AB_short_list = list(AB_set)
    ws.write(row, 0, gene_short)
    ws.write(row, 1, ", ".join(AB_short_list))
    row += 1

# Close the Excel file
wb.close()
