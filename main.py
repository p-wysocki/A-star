"""
A* algorithm

Usage:
  main.py GRAPH_FILEPATH
"""

import os
import graph_utils, file_utils
import pathfinding, config
from docopt import docopt


def main() -> None:

	args = docopt(__doc__)
	datafile = args['GRAPH_FILEPATH']

	# retrieve constants
	GRAPHS_DATAFILES_PATH = config.GRAPHS_DATAFILES_PATH

	# retrieve raw graph data
	raw_graph_data = file_utils.read_file(os.path.join(GRAPHS_DATAFILES_PATH, datafile))

	# get start and end node
	start_point, end_point = graph_utils.get_route(graph_data=raw_graph_data)

	# get graph description from datafile
	graph_description = graph_utils.get_graph_description(graph_data=raw_graph_data, end_point=end_point)

	route = graph_utils.get_route(graph_data=raw_graph_data)

	# find path using A*
	path_found = pathfinding.a_star(route=(start_point, end_point),
									graph_description=graph_description)
	
	# display results
	if path_found:
		for node in path_found:
			print(node, end=' ')
	else:
		print('Brak')

if __name__ == '__main__':
	main()
	



