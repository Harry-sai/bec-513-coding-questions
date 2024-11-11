import matplotlib.pyplot as plt
import numpy as np

# Step 1: Load data from the TSV file into a NumPy array.
data = np.loadtxt("demo_file.tsv", delimiter="\t")

# Step 2: Set up the figure dimensions.
plt.figure(figsize=(3, 10))  # Adjust the figure size as needed for better visualization.

# Step 3: Create the heatmap using the data, with a color map 'hot' and nearest interpolation.
plt.imshow(data, cmap='hot', interpolation='nearest', aspect='auto')

# Step 4: Add a color bar on the right to show the scale of intensity values.
plt.colorbar(orientation='vertical')

# Step 5: Set the plot title and axis labels for clarity.
plt.title("CTCF ChIP Peaks with Motif")
plt.xlabel("MNase Fragment Profile")
plt.ylabel("CTCF ChIP Peaks with Motif")

# Step 6: Customize x-axis and y-axis ticks to fit the data's range.
plt.xticks([0, 2000], [0, 2000])  # x-axis ticks and labels
plt.yticks([0, 20000, 40000, 60000, 80000, 100000], [0, 20000, 40000, 60000, 80000, 100000])  # y-axis ticks and labels

# Step 7: Invert the y-axis to match the preferred orientation.
plt.gca().invert_yaxis()

