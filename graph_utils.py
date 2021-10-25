import numpy as np
import file_utils
from typing import List

def get_adjacency_matrix(graph_datafile_path: str) -> np.array:
	"""
	Convert custom graph data into an adjacency matrix.

	Arguments:
		graph_data - custom graph data provided by the course
			instructor
	Returns:
		Adjacency matrix in form of a numpy array; values
		in the matrix correspond to the edges' weights.
	"""
	# retrieve raw graph data
	graph_data = file_utils.read_file(graph_datafile_path)

	# cut first two rows
	graph_data = graph_data[2:]

	# convert values to float and put into lists
	list_of_rows = []
	for string_values_line in graph_data:
		numeric_values_line = [float(i) for i in string_values_line.split()]
		list_of_rows.append(numeric_values_line) 

	# create numpy array out of them
	return np.array(list_of_rows)