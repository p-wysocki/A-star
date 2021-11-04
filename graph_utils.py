import numpy as np
import file_utils
import re
from typing import List, Dict, Tuple

def get_adjacency_matrix(graph_data: str) -> np.array:
	"""
	Convert custom graph data into an adjacency matrix.

	Arguments:
		graph_data - custom graph data provided by the course
			instructor
	Returns:
		Adjacency matrix in form of a numpy array; values
		in the matrix correspond to the edges' weights.
	"""

	# cut first two rows
	graph_data = graph_data[2:]

	# convert values to float and put into lists
	list_of_rows = []
	for string_values_line in graph_data:
		numeric_values_line = [float(i) for i in string_values_line.split()]
		list_of_rows.append(numeric_values_line) 

	# create numpy array out of them
	return np.array(list_of_rows)


def get_node_coordinates(graph_data: str) -> List[List[int]]:
	"""
	Return coordinates of all nodes in graph

	Arguments:
		graph_data - raw datafile contents
	Returns:
		list of [x, y] coordinates
	"""
	# choose only the first row
	graph_data = graph_data[0]

	consecutive_digits = [int(char) for char in graph_data if char.isdigit()]
	
	node_coordinates = [[consecutive_digits[i], consecutive_digits[i+1]] for i
						in range(0, len(consecutive_digits), 2)]

	return node_coordinates


def get_route(graph_data: str) -> Tuple[int, int]:
	"""
	Return route specified in graph datafile.

	Arguments:
		graph_data - raw datafile contents
	Returns:
		(start, end)
	"""
	raw_route = graph_data[1]
	start, end = raw_route.split(' ')
	return (start, end)


def get_graph_description(graph_data: str, end_point: int) -> Dict:
	"""
	Return a custom data structure describing a graph.

	Arguments:
		graph_data - raw datafile contents
		end_point - the end of algorithm's path, necessary for
			calculating heuristics
	Returns:
		graph_description{
			adjacency_matrix,
			nodes{
				coordinates{}
				heuristics{}
			}
		}
	"""
	graph_description = {}
	node_coordinates = {}
	raw_node_coordinates = get_node_coordinates(graph_data)

	# create a dict entry for every node and assign its coordinates
	for i, node in enumerate(raw_node_coordinates):
		single_node_coordinates = {'coordinates': node}
		node_coordinates[i] = single_node_coordinates
	graph_description['nodes'] = node_coordinates

	# add adjacency matrix
	graph_description['adjacency_matrix'] = get_adjacency_matrix(graph_data)

	# calculate node heuristics and add them to the dict
	end_point = graph_description['nodes'][end_point]['coordinates']
	for node_number in graph_description['nodes'].keys():
		graph_description['nodes'][node_number]['heuristic'] = get_euclidean_distance(
			end_point,
			graph_description['nodes'][node_number]['coordinates'])

	return graph_description


def get_euclidean_distance(point_a: Tuple[int, int], point_b: Tuple[int, int]) -> int:
	x_a, y_a = point_a
	x_b, y_b = point_b
	return ((((x_b - x_a )**2) + ((y_b-y_a)**2) )**0.5)


def get_node_neighbours(node: int, adjacency_matrix: np.array) -> List[Tuple[int, int]]:
	"""
	Arguments:
		node - number of the central node
		adjacency_matrix - taken from graph datafile
	Returns:
		list of (node_number, edge_weight)
	"""
	neighbours = {}
	for i, value in enumerate(adjacency_matrix[node]):

		# if there's an edge
		if value != 0:
			neighbours[i] = value

	return neighbours
