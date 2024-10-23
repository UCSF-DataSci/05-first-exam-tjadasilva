import sys

# Function to return the complement of a DNA sequence
def complement(sequence):
    # Dictionary mapping each base to its complement
    complement_map = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    
    # Generate complement sequence by replacing each base with its complement
    return ''.join([complement_map[base.upper()] for base in sequence])

# Function to return the reverse of a DNA sequence
def reverse(sequence):
    # Reverse the sequence using Python slicing
    return sequence[::-1]

# Function to return the reverse complement of a DNA sequence
def reverse_complement(sequence):
    # First get the complement, then reverse it
    return reverse(complement(sequence))

# Main function to handle command-line arguments and output results
def main():
    # Check if a DNA sequence was passed as a command-line argument
    if len(sys.argv) < 2:
        print("Usage: python dna_operations.py <DNA_SEQUENCE>")
        sys.exit(1)

    # Get the DNA sequence from command-line argument
    dna_sequence = sys.argv[1]
    
    # Ensure sequence is uppercase for consistency
    dna_sequence = dna_sequence.upper()

    # Perform DNA operations
    comp_seq = complement(dna_sequence)
    rev_seq = reverse(dna_sequence)
    rev_comp_seq = reverse_complement(dna_sequence)

    # Print the results
    print(f"Original sequence: {dna_sequence}")
    print(f"Complement: {comp_seq}")
    print(f"Reverse: {rev_seq}")
    print(f"Reverse complement: {rev_comp_seq}")

# Execute the main function when the script is run
if __name__ == "__main__":
    main()
