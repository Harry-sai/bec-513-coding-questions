import pandas as pd
import sys

# Command-line arguments for input file and output file
select_file = sys.argv[1]  # File containing terms to select
output_file = sys.argv[2]  # Output file for matched lines

# Load the terms to match from the input file
selection_df = pd.read_csv(select_file, names=['Column'])
search_terms = set(selection_df['Column'])  # Convert terms to a set for faster lookup

# Open the output file and write lines that match any term in search_terms
with open(output_file, 'w') as output:
    for input_line in sys.stdin:
        if any(term in input_line for term in search_terms):
            output.write(input_line)

