#!/usr/bin/env python3
# Script that compares the genes from both reference lists (RESF & BN) and prints the following:

# Both gene lists below were copied from the RESF_reflist.xlsx and BN_reflist.xlsx files

genes_RESF = ["blaTEM-1C", "aph(6)-Id", "aph(3'')-Ib", "aadA1", "blaTEM-1B", "sul3", "dfrA1", "tet(A)", "sul2",
              "dfrA5", "aadA2b", "cmlA1", "sul1", "aac(3)-IIa", "aac(6')-Ib-cr", "blaOXA-1", "catB3", "aac(3)-IId",
              "qnrS1", "qnrE1", "blaACT-2", "blaACT-1", "dfrA14", "floR", "aadA5", "blaCTX-M-15", "dfrA17", "mph(A)",
              "tet(B)", "blaSHV-1", "blaSHV-102", "blaSHV-48", "blaCARB-2", "dfrA16", "blaCTX-M-1", "lnu(F)", "aph(3')-Ia",
              "aadA2", "blaTEM-34", "dfrA12", "tet(M)", "blaTEM-1A", "qnrB19", "blaTEM-135", "blaTEM-126", "blaTEM-106", "blaTEM-220", 
              "bleO", "catA1", "blaTEM-52C", "mph(B)", "ere(A)", "dfrA7", "blaOXA-2", "dfrA29", "ant(3'')-Ia", "dfrA36", 
              "blaTEM-33", "blaTEM-40", "erm(B)", "dfrA8", "ant(2'')-Ia", "blaTEM-54", "tet(D)", "blaTEM-1D", "blaTEM-206",
              "blaTEM-141", "blaTEM-216", "blaTEM-214", "blaTEM-209", "aadA22", "cml", "tet(C)","aph(4)-Ia", "aac(6')-Ib", 
              "blaSHV-12", "blaOXA-9", "aac(3)-VIa", "blaTEM-213",
              "blaTEM-128", "blaTEM-207", "blaTEM-186", "blaTEM-143", "blaTEM-127", "blaTEM-95", "blaTEM-76",
              "blaTEM-30", "blaTEM-234", "blaTEM-217", "blaTEM-215", "blaTEM-208", "blaTEM-198", "blaTEM-176", 
              "blaTEM-166", "blaTEM-148", "blaTEM-105", "blaTEM-70", "aac(6')-Ib3", "blaTEM-24", "aac(3)-IV",
              "aadA24", "aph(3')-Ib", "blaSHV-3", "blaSHV-44", "OqxB", "OqxA", "blaSHV-5", "fosA6"]

genes_BN = ["mdf(A)", "aac(6')-Ib-cr", "blaOXA-1", "aac(3)-IIa", "sul1", "aac(3)-IId", "blaTEM-1B", "floR", "blaACT-1", 
            "dfrA14", "qnrS1", "tet(A)", "dfrA17", "blaCTX-M-15", "mph(A)", "dfrA1", "sul2", "tet(B)", "blaSHV-1",
            "dfrA5", "cmlA1", "dfrA16", "sul3", "blaCARB-2", "blaCTX-M-1", "blaZ", "dfrK", "aac(6')-aph(2'')", "tet(M)",
            "mecA", "dfrA12", "blaTEM-34", "blaTEM-1A", "blaTEM-1C", "qnrB19", "catA1", "aph(3')-IIb", "blaOXA-50", "fosA",
            "catB7", "blaPAO", "ant(2'')-Ia", "dfrA7", "dfrA29", "blaOXA-2", "dfrA36", "blaTEM-33", "blaTEM-40", "dfrA8",
            "catB3", "tet(C)", "blaSHV-12", "aac(6')-Ib", "blaOXA-9", "aac(3)-VIa", "aac(6')-Ib3", "blaTEM-24", "aac(3)-IV",
            "blaTEM-1D", "blaSHV-3", "oqxB", "oqxA", "blaTEM-54", "tet(D)", "blaTEM-52C"
]

print(f"Amount of genes in RESF list : {len(genes_RESF)}")

print(f"Amount of genes in BN list : {len(genes_BN)}")

# Convert the lists to sets
RESF = set(genes_RESF)
BN = set(genes_BN)

# Intersection: RESF & BN
print(f"Intersection: {len(RESF & BN)} genes occur in both sets")

# Union: RESF | BN
print(f"Union: {len(RESF | BN)} unique genes from both sets") 

# Differences: RESF - BN
print("Difference: {}".format(RESF - BN))
print("Difference: {}".format(BN - RESF))
