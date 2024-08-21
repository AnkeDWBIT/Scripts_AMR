#!/usr/bin/env python
# Script to go through the CARD raw data of the E. coli WGS & create a reference list of all the genes found and their corresponding resistance phenotypes/antibiotics

# Importing the required libraries
import os
import xlsxwriter

# Define the input-dir & output-file
input_dir = "/home/anked/BIT11_Traineeship/Ecoli_AMR/RGI_CARD/Ecoli_WGS/RGI_output/"
output_file = "/home/anked/BIT11_Traineeship/Ecoli_AMR/CARD_reflist.xlsx"

# STEP 1 : Retrieve data from the input_dir and save it in a dictionary
############################################################################################################################################################

# Initialize the dictionary to store the data
data_dict = {}

# Loop through the input directory
data_dict = {}
for subdir, dirs, files in os.walk(input_dir):
    sample = os.path.basename(subdir)
    for file in files:
        if file.endswith(".txt"):
            file_path = os.path.join(subdir, file)

            # Read the text file
            with open(file_path, 'r') as file:
                for line in file:
                    select_crit = line.split('\t')[5]

                    # Only look at genes having a "Perfect" or "Strict" select criteria (& not "Loose")
                    if select_crit == "Perfect" or select_crit == "Strict":
                        gene_name = line.split('\t')[8].strip()
                        antibiotics = line.split('\t')[27].strip()

                        # Add the genes and their associated antibiotics to the dictionary
                        if gene_name not in data_dict:
                            data_dict[gene_name] = [antibiotics]
                        else:
                            if antibiotics not in data_dict[gene_name]:
                                data_dict[gene_name].append(antibiotics)
                            else:
                                continue
                    
# STEP 2 : Create an Excel file to store the reference list
############################################################################################################################################################
wb = xlsxwriter.Workbook(output_file)
ws = wb.add_worksheet("CARD_reflist")
# Write the header line
header = ["Gene", "Antibiotic"]
ws.write_row(0, 0, header)

# Write the data to the Excel file
row = 2
for gene, AB_list in data_dict.items():
    AB_set = set(AB_list)
    AB_short_list = list(AB_set)
    ws.write(row, 0, gene)
    ws.write(row, 1, ", ".join(AB_short_list))
    row += 1

# Close the Excel file
wb.close()

# Print a message when the Excel-file is succesfully finished
print(f"Reference list has been created successfully and saved as {output_file}.")

