#!/bin/bash
# This script is used to run ResFinder for multiple E. coli strains (FASTA-files) at once
# Creates and output folder, also creates a subfolder for each strain to avoid overwriting of results


# VALIDATE INPUT
function usage(){
	errorString="This script requires 2 parameters: 1. Full path to folder with input FASTA files. 2. Full path to output folder (will create if it doens't exist yet).";

	echo -e ${errorString};
	exit 1;
}
if [ "$#" -ne 2 ]; then
	usage
fi

# 1. INPUT FOLDER CONTAINING .fasta files
inputFolder=$1;
# Remove trailing slash if this is last char
len=${#inputFolder};
lastPos=$(expr $len - 1);
lastChar=${inputFolder:$lastPos:1};
if [[ $lastChar == '/' ]]; then
	inputFolder=${inputFolder:0:$lastPos};
fi


# 2. OUTPUT FOLDER
outputFolder=$2
# Check if the directory exists
if [ ! -d "$outputFolder" ]; then
    # If it doesn't exist, create it
    mkdir -p "$outputFolder"
    echo "Output folder created."
else
    echo "Output folder already exists."
fi


# 3. RUN RESFINDER FOR ALL E.COLI STRAINS
# Concatenate filenames
for i in $(ls ${inputFolder}/*.fasta); do
	inputFile="${i}";
    # Remove .fasta
    posKeep=$(expr ${#i} - 6);
	baseNameTmp=${i:0:$posKeep};
    # Remove path to get strain number for output folder
	baseName=${baseNameTmp/"$inputFolder"/""};
    # Remove leading slash, if present
    baseName="${baseName#/}";
    
    # Make an output-subfolder for each strain to avoid overwriting
    outputFolderStrain="${outputFolder}/${baseName}";
    mkdir -p ${outputFolderStrain};

    # Show inputfiles
    echo "### Inputfile: $inputFile (basename: $baseName) ###";
    echo "### Running ResFinder ###";

    # Compose command
    Command="python -m resfinder -ifa ${inputFile} -o ${outputFolderStrain} -b /usr/bin/blastn -s 'Escherichia coli' -db_res /home/guest/BIT11_Traineeship/Ecoli_AMR/ResFinder_2/resfinder_db -acq -c -db_point /home/guest/BIT11_Traineeship/Ecoli_AMR/ResFinder_2/pointfinder_db -u";
    if [ "$4" = "y" ]; then
    Command="$Command -x"
fi

#     
    # Show command
    echo -e "$Command";

    # Execute
   output=$(eval $Command);

    # Show output
   echo -e "$output";


done