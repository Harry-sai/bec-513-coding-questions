library(dplyr)
library(tidyverse)

# Step 1: Get file paths from the command-line arguments.
input_file = readLines(commandArgs(trailingOnly = TRUE)[1])

# Step 2: Initialize an empty variable for storing merged data.
merged_data <- NULL

# Step 3: Loop through each file path in the list.
for (file_path in input_file) {
  # Check if the file exists.
  if (file.exists(file_path)) {

    # Step 4: Read the data from the current file (tab-separated, without column names).
    new_data <- read_delim(file_path, delim = "\t", col_names = FALSE, show_col_types = FALSE)

    # Step 5: If merged_data is empty, assign it the first file's data.
    # Otherwise, merge current file data by the first column "X1".
    if (is.null(merged_data)) {
      merged_data <- new_data
    } else {
      merged_data <- merged_data %>%
        inner_join(new_data, by = c("X1" = "X1"))
    }
  } else {
    # Display a warning if the file does not exist.
    warning(paste("File not Found:", file_path))
  }
}

# Step 6: Write the merged data to the standard output.
write_tsv(merged_data, stdout())

