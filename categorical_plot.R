library(ggplot2)
library(readr)
library(stringr)

args <- commandArgs(trailingOnly = TRUE)

output_plot <- args[1]
col_names <- str_split(args[2], ",")[[1]]


data <- read.table(file("stdin"),sep='\t',header = FALSE)

colnames(data) <- col_names

x_col <- col_names[1]
y_col <- col_names[2]
category_col <- col_names[3]

plot <- ggplot(data, aes(x = .data[[x_col]], y = .data[[y_col]], group = .data[[category_col]], color = .data[[category_col]])) +
	geom_line(linewidth = 0.5) +
	geom_point(size = 0.5) +
	labs(title = "Multiple line plot" , x = x_col , y = y_col) +
	theme_bw()

ggsave(output_plot, plot)
print(plot)
