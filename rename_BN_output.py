#!/usr/bin/env python
# Script to rename the output files from BioNumerics to the sample name MTTxxx

# Importing the required libraries
import os

# Specify the input directory containing the BioNumerics output files
input_dir = "/home/guest/BIT11_Traineeship/Ecoli_AMR/BioNumerics_out"

# Go through each file in the input directory
files = os.listdir(input_dir)
for file in files : 
    # Take the last 3 characters of the file name & place MTT in front of it
    sample = "MTT" + file[-3:]
    #print(f"Renaming file {file} to {sample}")
    # Rename the file
    os.rename(os.path.join(input_dir, file), os.path.join(input_dir, sample))
    print(f"Renamed file {file} to {sample}")