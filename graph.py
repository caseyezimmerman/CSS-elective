def depth_first_traversal(graph, start):
	visited = {}


	for key in graph:
		visited[key] = False

	print start
	visited[start] = True

	stack = [ start ]

	while len(stack) !=0:
		last_index = len(stack) - 1
		last_node = stack[last_index]

		neighbors = graph[last_node]
		first_unvisited_neighbor = None

		for neighbor in neighbors:
			if visited[neighbor] == False:
				first_unvisited_neighbor = neighbor

		if first_unvisited_neighbor is None:
			del stack[last_index]
		else:
			print first_unvisited_neighbor
			visited[first_unvisited_neighbor] = True
			stack.append[first_unvisited_neighbor]

	print stack
	print visited


    

graph = {
  "A" : ["B", "C", "D", "E"],
  "B" : ["A", "C", "E"],
  "C" : ["A", "B"],
  "D" : ["A", "E"],
  "E" : ["A", "B"]
}

depth_first_traversal(graph, "A")