import os
import graph_utils, config


def main() -> None:

	# retrieve constants
	NUMBER_OF_GRAPH_DATAFILES = config.NUMBER_OF_GRAPH_DATAFILES
	GRAPHS_DATAFILES_PATH = config.GRAPHS_DATAFILES_PATH

	# list of files containing graph data
	graph_datafiles = [f'{i}.txt' for i in range(1, NUMBER_OF_GRAPH_DATAFILES)]

	# convert them into adjacency matrices
	adjacency_matrices = []
	for datafile in graph_datafiles:
		datafile_path = os.path.join(GRAPHS_DATAFILES_PATH, datafile)
		adjacency_matrix = graph_utils.get_adjacency_matrix(datafile_path)
		adjacency_matrices.append(adjacency_matrix)

	for i in adjacency_matrices:
		print(i)

if __name__ == '__main__':
	main()
	



