"""
A* algorithm

Usage:
  main.py GRAPH_FILEPATH START_NODE END_NODE
"""

import os
import graph_utils, file_utils, config
from docopt import docopt


def main() -> None:

	#args = docopt(__doc__)
	datafile = '1.txt'
	start_point = 0
	end_point = 3

	# retrieve constants
	GRAPHS_DATAFILES_PATH = config.GRAPHS_DATAFILES_PATH

	# retrieve raw graph data
	raw_graph_data = file_utils.read_file(os.path.join(GRAPHS_DATAFILES_PATH, datafile))

	# get graph description from datafile
	graph_description = graph_utils.get_graph_description(graph_data=raw_graph_data, end_point=end_point)
	adjacency_matrix = graph_description['adjacency_matrix']

	
	print(graph_utils.get_node_neighbours(node=3, adjacency_matrix=adjacency_matrix))

if __name__ == '__main__':
	main()
	



