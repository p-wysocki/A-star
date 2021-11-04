from typing import List, Tuple
import math
import graph_utils


def a_star(route: Tuple[int, int], graph_description: dict) -> List[int]:
	
	start, end = route
	nodes_to_visit = {start}
	came_from = {}

	# heuristics for each node
	node_heuristics = {i: graph_description['nodes'][i]['heuristic'] for i in graph_description['nodes']}

	# cost of traversal from start to node
	start_to_node = {i: float('inf') for i in graph_description['nodes']}
	start_to_node[start] = 0

	combined_start_to_node = {i: float('inf') for i in graph_description['nodes']}
	combined_start_to_node[start] = node_heuristics[start]

	adjacency_matrix = graph_description['adjacency_matrix']
	
	while nodes_to_visit:
		print('nodes to visit', nodes_to_visit)

		# find neighbouring node with the lowest traversal cost 

		# get rid of nodes not in nodes_to_visit
		total_weights_copy = combined_start_to_node
		total_weights_copy = {k: total_weights_copy[k] for k in nodes_to_visit if k in total_weights_copy}

		# select the cheapest one
		cheapest_node_to_visit = min(total_weights_copy, key=total_weights_copy.get)

		if cheapest_node_to_visit == end:
			print(trace_path(came_from, cheapest_node_to_visit))
			return

		nodes_to_visit.remove(cheapest_node_to_visit)

		next_node_neighbours = graph_utils.get_node_neighbours(node=cheapest_node_to_visit,
															   adjacency_matrix=adjacency_matrix)

		for neighbour in next_node_neighbours:
			temp_start_to_node_cost = start_to_node[cheapest_node_to_visit] + next_node_neighbours[neighbour]

			if temp_start_to_node_cost < start_to_node[neighbour]:
				came_from[cheapest_node_to_visit] = neighbour
				start_to_node[neighbour] = temp_start_to_node_cost
				combined_start_to_node[neighbour] = start_to_node[neighbour] + node_heuristics[neighbour]

				if neighbour not in nodes_to_visit:
					nodes_to_visit.add(neighbour)

	print('FAIL')
	return


def trace_path(came_from: dict, current_node: int):
	print(came_from)
	reconstructed_path = []
	while came_from[current_node]:
		current_node = came_from[current_node]
		reconstructed_path.insert(0, current_node)

	return reconstructed_path
