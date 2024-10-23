import sys
import re

# Function to read the DNA sequence from the FASTA file and remove whitespaces
def read_fasta(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()

    # Ignore the header (first line starting with '>') and join the remaining lines
    sequence = ''.join(line.strip() for line in lines if not line.startswith('>'))

    # Remove any potential whitespaces from the sequence
    return sequence.replace(' ', '').replace('\n', '')

# Function to find all occurrences of the cut site
def find_cut_sites(sequence, cutsite):
    # Remove the '|' from the cutsite
    cutsite_clean = cutsite.replace('|', '')
    
    # Find all occurrences of the cutsite in the sequence
    cut_positions = [match.start() for match in re.finditer(cutsite_clean, sequence)]

    return cut_positions

# Function to find cut site pairs that are 80-120 kb apart
def find_cut_site_pairs(cut_positions, min_distance=80000, max_distance=120000):
    cutsite_pairs = []
    
    # Compare each cutsite position with every other cutsite to find pairs within the distance range
    for i in range(len(cut_positions)):
        for j in range(i + 1, len(cut_positions)):
            distance = cut_positions[j] - cut_positions[i]
            if min_distance <= distance <= max_distance:
                cutsite_pairs.append((cut_positions[i], cut_positions[j]))
    
    return cutsite_pairs

# Main function
def main():
    if len(sys.argv) < 3:
        print("Usage: python find_cutsites.py <FASTA_FILE_PATH> <CUT_SITE>")
        sys.exit(1)

    # Get arguments: FASTA file path and cut site sequence
    fasta_filepath = sys.argv[1]
    cutsite = sys.argv[2]

    # Read the DNA sequence from the FASTA file
    dna_sequence = read_fasta(fasta_filepath)

    # Find all cut site locations
    cut_positions = find_cut_sites(dna_sequence, cutsite)

    # Find pairs of cut sites 80-120kb apart
    cutsite_pairs = find_cut_site_pairs(cut_positions)

    # Output the results
    total_pairs = len(cutsite_pairs)
    print(f"Analyzing cut site: {cutsite}")
    print(f"Total cut sites found: {len(cut_positions)}")
    print(f"Cut site pairs 80-120 kbp apart: {total_pairs}")
    print("First 5 pairs:")
    for i, (pos1, pos2) in enumerate(cutsite_pairs[:5], 1):
        print(f"{i}. {pos1} - {pos2}")

    # Save the results in the results directory
    with open('bioinformatics_project/results/cutsite_summary.txt', 'w') as summary_file:
        summary_file.write(f"Analyzing cut site: {cutsite}\n")
        summary_file.write(f"Total cut sites found: {len(cut_positions)}\n")
        summary_file.write(f"Cut site pairs 80-120 kbp apart: {total_pairs}\n")
        summary_file.write("First 5 pairs:\n")
        for i, (pos1, pos2) in enumerate(cutsite_pairs[:5], 1):
            summary_file.write(f"{i}. {pos1} - {pos2}\n")

    print(f"Results saved to bioinformatics_project/results/cutsite_summary.txt")

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
