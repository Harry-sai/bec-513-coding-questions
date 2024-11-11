# Q1: Selecting lines from stdin (Python Code + Linux Command)# bec-513-coding-questions
## Filtering Data Based on Selected Terms

This project includes a Python script that extracts specific lines from a large data file based on a set of terms provided in a separate file. It’s designed for efficient data filtering in genomics or other datasets where pattern matching in compressed files is useful.


1. **Input Files**:
   - **Data File**: A large `.tsv.gz` file (`q1_data.tsv.gz`) with the main dataset.
   - **Selection File**: A plain text file (`to_select.tsv`) listing terms to match.

2. **Command Execution**:
   Use the following command to run the filter:

   ```bash
   zless data/q1_data.tsv.gz | awk 'NR==1||/ENSG/' | python3 selecting_lines.py data/to_select.tsv outputfile_new.tsv
   ```

   - **Explanation**:
     - `zless` decompresses and streams the data file.
     - `awk 'NR==1||/ENSG/'` retains only the header and lines containing "ENSG" (useful for filtering specific IDs or genes).
     - `python3 selecting_lines.py` takes:
       - `data/to_select.tsv` to define matching terms.
       - `outputfile_new.tsv` to save matched lines.

3. **Output**:
   - The output file (`outputfile_new.tsv`) will contain only the lines from the data file that match any term in the selection file.

# Q2: Plotting a group of lines ( R + Linux Command)
This R script, `<your code.R>`, reads data from standard input, assigns custom column names, and creates a multi-line plot grouped by categories. It’s useful for visualizing trends across multiple groups.

1. **Purpose**:
   - Reads tab-separated data, assigns specified column names, and plots grouped data lines.

2. **Running the Script**:
   - Use the following command to run the script:
     ```bash
     cat data/q2_data.tsv | Rscript <your code.R> "different_clusters.png" "Relative from center [bp],Enrichment over Mean,MNase fragment profile"
     ```

3. **Explanation of the Command**:
   - `cat data/q2_data.tsv`: Streams the data file to standard input.
   - `Rscript <your code.R> "different_clusters.png" "Relative from center [bp],Enrichment over Mean,MNase fragment profile"`:
     - `<your code.R>`: Runs the script.
     - `"different_clusters.png"`: Specifies the output plot file.
     - `"Relative from center [bp],Enrichment over Mean,MNase fragment profile"`: Column names for x-axis, y-axis, and category.

4. **Output**:
   - A multi-line plot is saved to the specified file (`different_clusters.png`), showing each category in a different color, with custom axis labels.

# Q3: Merge multiple files (R + Linux Command)
This script, `join_list_of_file.R`, merges multiple files on a common key column (`X1`). Here’s how it works and how to use it:

1. **Purpose**: 
   - Reads multiple files specified in a list, verifies file existence, and merges them based on a common column (`X1`), outputting the combined data.

2. **Running the Script**:
   - Use the following command to execute the script:
     ```
     cat data/q2_data.tsv | Rscript join_list_of_file.R
     ```

3. **Explanation of the Command**:
   - `cat data/q2_data.tsv` provides a list of file paths.
   - `Rscript join_list_of_file.R` executes the script with these files as input.

4. **Output**:
   - The final merged data is written to standard output, which can be redirected or piped as needed.

# Q4: Label with quantiles (Python)
This script, `group_in_quantiles.py`, divides a numeric dataset into quantiles, labeling each data point according to its quantile group.

1. **Purpose**: 
   - Reads a list of numbers from standard input and assigns each value to a specified number of quantiles.

2. **Running the Script**:
   - Use the following command to run the script:
     ```bash
     cat data/first_hundred_numbers.tsv | python group_in_quantiles.py 4
     ```

3. **Explanation of the Command**:
   - `cat data/first_hundred_numbers.tsv` reads the data file.
   - `python group_in_quantiles.py 4` runs the script, dividing values into 4 quantiles.

4. **Output**:
   - The script outputs a table showing the original values, assigned quantile labels (e.g., `q1`, `q2`, etc.), and the range for each quantile.

# Q5: Plotting big matrix
This script, `heatmap.py`, visualizes numerical data from a TSV file as a vertical heatmap. It’s designed for showing peak intensities, such as MNase-seq or ChIP-seq patterns, with color-coded values.

1. **Purpose**: 
   - Reads a data file (`demo_file.tsv`) and creates a heatmap, representing the intensity of CTCF ChIP peaks.

2. **Running the Script**:
   - The following commands prepare the data file and generate the heatmap:
     ```bash
     zcat data/big_data.tsv.gz | cut --complement -f1 > demo_file.tsv
     python3 heatmap.py
     ```

3. **Explanation of Commands**:
   - `zcat data/big_data.tsv.gz | cut --complement -f1 > demo_file.tsv`: 
     - Decompresses `big_data.tsv.gz` and removes the first column.
     - Outputs the result to `demo_file.tsv` for further processing.
   - `python3 heatmap.py`: Generates the heatmap using `demo_file.tsv` as input.

4. **Output**:
   - The script displays a heatmap with:
     - X-axis: "MNase Fragment Profile" with custom tick labels.
     - Y-axis: "CTCF ChIP Peaks with Motif" with an inverted scale to fit data orientation.
     - A vertical color bar indicating intensity.

