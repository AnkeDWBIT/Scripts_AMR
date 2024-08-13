#!/usr/bin/env python
# Script to go through the ResFinder raw data in files named "pheno_table.txt" of the E. coli WGS & create a reference list of all the genes found and their corresponding resistance phenotypes/antibiotics

# Importing the required libraries
import os
import xlsxwriter

# Define the input-dir & output-file
input_dir = "/home/guest/BIT11_Traineeship/Ecoli_AMR/ResFinder_tool/resfinder_output"
output_file = "/home/guest/BIT11_Traineeship/Ecoli_AMR/RESF_reflist.xlsx"

# STEP 1 : Retrieve data from the input_dir and save it in a dictionary
############################################################################################################################################################
# Loop through the input directory and look for the files named "pheno_table.txt"
data_dict = {}
for subdir, dirs, files in os.walk(input_dir):
    sample = os.path.basename(subdir)
    for file in files:
        if file == "pheno_table.txt" :
            file_path = os.path.join(subdir, file)
            #print(f"Found data for sample {sample} in file {file}")
            # Read the text file
            with open(file_path, 'r') as file:
                lines = file.readlines()

                # Flags for processing lines
                process_lines = False
                
                # Iterate through the lines
                for line in lines:
                    # Strip the line of leading/trailing whitespaces
                    line = line.strip()
                      
                    # Skip empty lines
                    if not line:
                        continue
                
                    # Start processing after the line starting with "# Antimicrobial"
                    if line.startswith("# Antimicrobial"):
                        process_lines = True
                        continue  # Skip the current header line

                    # Stop processing at the line starting with "# WARNING"
                    if line.startswith("# WARNING"):
                        break

                    # Process the lines only if the flag is set
                    if process_lines:

                        # Split the line into columns and retrieve phenotype, AB and gene
                        parts = line.split('\t')
                        phenotype = parts[2].strip()
                        if phenotype == "Resistant":
                            antibiotic = parts[0].strip()
                            genes = parts[4].strip() # Genes are only present when the phenotype is "Resistant"
                            #print(f"\n {phenotype} - {antibiotic} - {genes}.")

                            # Split the genes into a list of genes
                            gene_list = genes.split(", ")
                            #print(f"Original Gene List : {gene_list}")

                            # Retain only short gene name
                            gene_list_short = [gene.split(" ")[0] for gene in gene_list]
                            #print(f"Shortened Gene List : {gene_list_short}")

                            # Make a dictionary with gene & linked ABs
                            for gene in gene_list_short:
                                if gene not in data_dict:
                                    data_dict[gene] = [antibiotic]
                                else:
                                    if antibiotic not in data_dict[gene]:
                                        data_dict[gene].append(antibiotic)
                                    else:
                                        continue

#print(data_dict)
                     
# STEP 2 : Create an Excel file to store the reference list
############################################################################################################################################################
wb = xlsxwriter.Workbook(output_file)
ws = wb.add_worksheet("RESF_reflist")
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

# Print a message when the Excel-file is succesfully finished
print(f"Reference list has been created successfully and saved as {output_file}.")