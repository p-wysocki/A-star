from typing import List, Tuple
import math
import graph_utils


def a_star(route: Tuple[int, int], graph_description: dict) -> List[int]:
	"""
	Return a path from start to end node found with A* algorithm.

	Arguments:
		route - tuple of (start, end) nodes
		graph_description - custom graph_description from graph_utils

	Returns:
		list of consecutive nodes describing a path or None if there's no path 
	"""
	
	start, end = route
	nodes_to_visit = {start}
	came_from = {}

	# get data from graph_descriptor
	node_heuristics = {i: graph_description['nodes'][i]['heuristic'] for i in graph_description['nodes']}
	adjacency_matrix = graph_description['adjacency_matrix']

	# cost of traversal from start to node (only edge weights)
	start_to_node = {i: float('inf') for i in graph_description['nodes']}
	start_to_node[start] = 0

	# combined cost of traversal from start to node (edge weights + heuristic)
	combined_start_to_node = {i: float('inf') for i in graph_description['nodes']}
	combined_start_to_node[start] = node_heuristics[start]

	while nodes_to_visit:

		# get rid of nodes not in nodes_to_visit
		total_weights_copy = combined_start_to_node
		total_weights_copy = {k: total_weights_copy[k] for k in nodes_to_visit if k in total_weights_copy}

		# select the cheapest one
		cheapest_node_to_visit = min(total_weights_copy, key=total_weights_copy.get)

		# if A* reached the end, return the path
		if cheapest_node_to_visit == end:
			return trace_path(came_from, route)

		# we no longer need to visit this node
		nodes_to_visit.remove(cheapest_node_to_visit)

		next_node_neighbours = graph_utils.get_node_neighbours(node=cheapest_node_to_visit,
															   adjacency_matrix=adjacency_matrix)

		# check which neighbour is the most promising next point
		for neighbour in next_node_neighbours:
			temp_start_to_node_cost = start_to_node[cheapest_node_to_visit] + next_node_neighbours[neighbour]

			# compare weights
			if temp_start_to_node_cost < start_to_node[neighbour]:
				came_from[cheapest_node_to_visit] = neighbour
				start_to_node[neighbour] = temp_start_to_node_cost
				combined_start_to_node[neighbour] = start_to_node[neighbour] + node_heuristics[neighbour]

				# if node looks promising, see what's deeper in it
				if neighbour not in nodes_to_visit:
					nodes_to_visit.add(neighbour)

	return None


def trace_path(came_from: dict, route: Tuple[int, int]):
	"""
	Return a list of consecutive nodes being an output of
	the A* algorithm.

	Arguments:
		came_from - information about algorithm's consecutive
			steps
		route - tuple of (start, end) nodes
	"""
	
	current_node, end = route
	reconstructed_path = [current_node]
	while current_node != end:
		current_node = came_from[current_node]
		reconstructed_path.append(current_node)

	# add 1 element wise to account for Python counting from 0
	reconstructed_path = [i+1 for i in reconstructed_path]

	return reconstructed_path
