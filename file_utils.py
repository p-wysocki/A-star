from typing import List

def read_file(file_path: str) -> List[str]:
	"""
	Return contents of a file.

	Return value is a list of strings which
	elements are consecutive lines.
	"""
	with open(file_path) as file:
		lines = file.readlines()

		# delete newlines
		lines = [line.rstrip() for line in lines]

	return lines