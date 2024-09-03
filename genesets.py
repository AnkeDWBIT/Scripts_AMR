#!/usr/bin/env python
# Script to compare genesets found in the data of 284 E. coli WGS analysed with the 4 bioinformatics tools (RESF, BN, RGI-CARD, AMRF+)

# Importing the required libraries
import os
import openpyxl
# Initialize lists to store gene sets per tool
RESF_genes = []
BN_genes = []
RGI_genes = []
AMRF_genes = []

# Specify the input file containing all reference lists & load the workbook
input_file = "/home/guest/BIT11_Traineeship/Ecoli_AMR/Reference_lists/reflists.xlsx"
wb = openpyxl.load_workbook(input_file)

# STEP 1: LOAD THE GENES FROM THE REFERENCE LISTS
####################################################################################################################################
# Load the RESF_reflist worksheet
ws_RESF = wb["RESF_reflist"]
for row in ws_RESF.iter_rows(min_row=3, max_row=ws_RESF.max_row, min_col=1, max_col=1):
    for cell in row:
        RESF_genes.append(cell.value.lower())

# Load the BN_reflist worksheet
ws_BN = wb["BN_reflist"]
for row in ws_BN.iter_rows(min_row=3, max_row=ws_BN.max_row, min_col=1, max_col=1):
    for cell in row:
        BN_genes.append(cell.value.lower())

# Load the RGI_reflist worksheet
ws_RGI = wb["CARD_reflist"]
for row in ws_RGI.iter_rows(min_row=3, max_row=ws_RGI.max_row, min_col=1, max_col=1):
    for cell in row:
        RGI_genes.append(cell.value.lower())

# Load the AMRF_reflist worksheet
ws_AMRF = wb["AMRF_reflist"]
for row in ws_AMRF.iter_rows(min_row=3, max_row=ws_AMRF.max_row, min_col=1, max_col=1):
    for cell in row:
        AMRF_genes.append(cell.value.lower())

# Convert the lists to sests
RESF = set(RESF_genes)
BN = set(BN_genes)
RGI = set(RGI_genes)
AMRF = set(AMRF_genes)

# STEP 2 : Compare the genesets e.g. overlap
####################################################################################################################################
# Intersection = Genes that occur in all 4 tools
intersection = RESF & BN & RGI & AMRF
RESF_BN_intersection = RESF & BN
RESF_RGI_intersection = RESF & RGI
RESF_AMRF_intersection = RESF & AMRF
BN_RGI_intersection = BN & RGI
BN_AMRF_intersection = BN & AMRF
RGI_AMRF_intersection = RGI & AMRF

#print(f"Intersection: {len(intersection)} genes occur in all 4 tools. \n They are: {intersection}")

# Union = non-redundant/unique genes from all 4 tools combined
all_genes = RESF | BN | RGI | AMRF
RESF_BN_union = RESF | BN
RESF_RGI_union = RESF | RGI
RESF_AMRF_union = RESF | AMRF
BN_RGI_union = BN | RGI
BN_AMRF_union = BN | AMRF
RGI_AMRF_union = RGI | AMRF

#print(f"Union: {len(all_genes)} unique genes from all 4 sets combined. \n They are: {all_genes}")

# % genes used by all 4 tools
percentage_shared = len(intersection) / len(all_genes) * 100
#print(f"Percentage of genes used by all 4 tools: {percentage_shared:.2f}%")


# STEP 3 : Write the results to an output file
####################################################################################################################################
output_file = "/home/guest/BIT11_Traineeship/Ecoli_AMR/compare_genesets.txt"
with open(output_file, 'w') as f:
    f.write("Amount of unique genes in each tool:\n")
    f.write("=====================================\n")
    f.write(f"RESF: {len(RESF)} genes\n")
    f.write(f"BN: {len(BN)} genes\n")
    f.write(f"RGI: {len(RGI)} genes\n")
    f.write(f"AMRF: {len(AMRF)} genes\n\n")
    f.write("Comparison of genesets:\n")
    f.write("=======================\n")
    f.write("1) Intersection = genes that occur in both sets\n")
    f.write(f"RESF & BN: {len(RESF_BN_intersection)} genes occur in both sets. \n")
    f.write(f"RESF & RGI: {len(RESF_RGI_intersection)} genes occur in both sets. \n")
    f.write(f"RESF & AMRF: {len(RESF_AMRF_intersection)} genes occur in both sets. \n")
    f.write(f"BN & RGI: {len(BN_RGI_intersection)} genes occur in both sets. \n")
    f.write(f"BN & AMRF: {len(BN_AMRF_intersection)} genes occur in both sets. \n")
    f.write(f"RGI & AMRF: {len(RGI_AMRF_intersection)} genes occur in both sets. \n\n")
    f.write(f"=> {len(intersection)} genes occur in all 4 sets. \n")
    f.write("---------------------------------------------- \n")
    f.write("2) Union = unique genes from both sets combined\n")
    f.write(f"RESF | BN: {len(RESF_BN_union)} unique genes from both sets combined. \n")
    f.write(f"RESF | RGI: {len(RESF_RGI_union)} unique genes from both sets combined. \n")
    f.write(f"RESF | AMRF: {len(RESF_AMRF_union)} unique genes from both sets combined. \n")
    f.write(f"BN | RGI: {len(BN_RGI_union)} unique genes from both sets combined. \n")
    f.write(f"BN | AMRF: {len(BN_AMRF_union)} unique genes from both sets combined. \n")
    f.write(f"RGI | AMRF: {len(RGI_AMRF_union)} unique genes from both sets combined. \n\n")
    f.write(f"=> {len(all_genes)} unique genes from all 4 sets combined. \n\n")
    f.write("---------------------------------------------- \n")
    f.write(f"3) Percentage of genes used by all 4 tools \n")
    f.write(f"{percentage_shared:.2f}%\n")


print(f"Results written to {output_file}")