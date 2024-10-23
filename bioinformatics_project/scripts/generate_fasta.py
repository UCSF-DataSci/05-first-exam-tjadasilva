import random
import textwrap

# Function to generate a random DNA sequence of specified length
def generate_dna_sequence(length):
    # DNA bases
    bases = ['A', 'C', 'G', 'T']
    # Generate random DNA sequence of given length
    return ''.join(random.choices(bases, k=length))

# Function to write the sequence in FASTA format
def save_fasta(sequence, filepath, line_length=80):
    # Open file in write mode
    with open(filepath, 'w') as fasta_file:
        # Write a simple header (optional)
        fasta_file.write(">random_sequence\n")
        # Wrap the sequence to the specified line length and write to the file
        wrapped_sequence = textwrap.wrap(sequence, line_length)
        fasta_file.write("\n".join(wrapped_sequence))

# Main function
def main():
    # Generate a random DNA sequence of 1 million base pairs
    dna_sequence = generate_dna_sequence(1000000)

    # Define the file path
    fasta_filepath = "bioinformatics_project/data/random_sequence.fasta"

    # Save the sequence in FASTA format with 80 base pairs per line
    save_fasta(dna_sequence, fasta_filepath)

    print(f"Random DNA sequence generated and saved to {fasta_filepath}")

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
