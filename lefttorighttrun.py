

def solve(maze):
	current = maze.start
	end = maze.end
	heading = 2
	path = []

	while current != end:
		path.append(current)
		if current.Neighbours[(heading-1)%4] != None: # if there is a path to the left
			heading = (heading - 1) % 4
			current = current.Neighbours[heading]
		elif current.Neighbours[heading] != None: # if there is a path straight ahead
			current = current.Neighbours[heading]
		elif current.Neighbours[(heading+1)%4] != None: # if there is one to the right
			heading = (heading + 1) % 4
			current = current.Neighbours[heading]
		else: # dead end
			heading = (heading + 2) % 4
			current = current.Neighbours[heading]

		# print(current.Position) # uncomment to debug pathing

	path.append(current) # appends the final node (end)

	# for node in path:
	# 	for neigh in node.Neighbours:
	# 		if neigh not in path:
	# 			neigh = None

	heading = 2
	refined_path = []
	current = maze.start
	while current != end:
		refined_path.append(current)
		neigh = current.Neighbours
		if neigh[(heading+1)%4] in path: # if there is one to the right
			heading = (heading + 1) % 4
			current = neigh[heading]
		elif neigh[heading] in path: # if there is a path straight ahead
			current = neigh[heading]
		elif neigh[(heading-1)%4] in path: # if there is a path to the left
			heading = (heading - 1) % 4
			current = neigh[heading]
		else: # turn around
			# path.append(current)
			# current = current.Neighbours[(heading+2)%4]
			# heading = (heading + 2) % 4
			print("huh")
	refined_path.append(current) # appends the final node (end)

	return refined_path