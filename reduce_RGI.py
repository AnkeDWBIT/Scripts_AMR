#!/usr/bin/env python
#Script to reduce the RGI data for each strain to only retain coumn 6 with cutoff, column 9 with best_hit_ARO or gene name, column 15 with drug class and column 28 with antibiotic

# Importing the required libraries
import openpyxl
import os
import re


# Specify input- & output directory
####################################################################################################################################
# Input directory with the RGI data
# input_dir = "/home/anked/BIT11_Traineeship/Ecoli_AMR/RGI_CARD/Ecoli_WGS/RGI_output/"
input_dir = "/home/guest/BIT11_Traineeship/Ecoli_AMR/Ruwe_data/CARD_subset15/"

# Make an output directory to store the reduced RGI data of each strain
#output_dir = "/home/guest/BIT11_Traineeship/Ecoli_AMR/RGI_CARD/Ecoli_WGS/RGI_output_reduced/"
output_dir = "/home/guest/BIT11_Traineeship/Ecoli_AMR/Ruwe_data/CARD_subset15_reduced/"

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Retrieve relevant info from RGI/CARD data
####################################################################################################################################
# Look in the input directory for the .txt files
files = [f for f in os.listdir(input_dir) if f.endswith(".txt")]

# Sort the files based on the numeric part of the sample ID (e.g., MTT001, MTT002)
files.sort(key=lambda f: int(re.search(r'\d+', f).group()))

# Go through each file
for file in files:
    
        # Open the .txt-files
        file_path = os.path.join(input_dir, file)
        with open(file_path) as f:

            # Open the output file to write the reduced RGI data
            output_file = file.replace(".txt", "_reduced.txt")
            with open(os.path.join(output_dir, output_file), "w") as out:
    
                # Go through each line in the file
                for line in f:
    
                    # Split the line into columns
                    columns = line.strip().split("\t")

                    if len(columns) >= 28 :
                        # Write the columns of interest to the output file
                        out.write("\t".join([columns[5], columns[8], columns[14], columns[27]]) + "\n")
                    else : 
                         # Write the columns of interest to the output file
                         out.write("\t".join([columns[5], columns[8], columns[14]]) + "\n")

# Print a message when the script has finished
print(f"RGI data has been reduced and stored in the output directory: {output_dir}")