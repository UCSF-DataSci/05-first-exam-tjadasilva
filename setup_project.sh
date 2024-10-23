#!/bin/bash

# Create main project directory
mkdir -p bioinformatics_project

# Create subdirectories: data, scripts, results
mkdir -p bioinformatics_project/data
mkdir -p bioinformatics_project/scripts
mkdir -p bioinformatics_project/results

# Create empty Python files in the scripts directory
touch bioinformatics_project/scripts/generate_fasta.py
touch bioinformatics_project/scripts/dna_operations.py
touch bioinformatics_project/scripts/find_cutsites.py

# Create an empty file in the results directory
touch bioinformatics_project/results/cutsite_summary.txt

# Create an empty FASTA file in the data directory
touch bioinformatics_project/data/random_sequence.fasta

# Create README.md with a brief description
echo "# Bioinformatics Project" > bioinformatics_project/README.md
echo "This project directory contains the following structure:" >> bioinformatics_project/README.md
echo "- **data/**: Contains input files for bioinformatics analysis (e.g., random_sequence.fasta)." >> bioinformatics_project/README.md
echo "- **scripts/**: Includes Python scripts for various operations (e.g., generate_fasta.py, dna_operations.py, find_cutsites.py)." >> bioinformatics_project/README.md
echo "- **results/**: Stores results of the bioinformatics analysis (e.g., cutsite_summary.txt)." >> bioinformatics_project/README.md

# Output success message
echo "Project directory structure created successfully:"
tree bioinformatics_project
