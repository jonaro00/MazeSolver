from collections import deque


def solve(maze):
	current = maze.start
	end = maze.end
	heading = 2
	headings = deque([])
	path = deque([])

	while current != end:
		neigh = current.Neighbours
		if current in path: # if there has been a loop -> dead end
			current = path.pop()
			current.Neighbours[heading] = None
			headings.pop()
			heading = headings.pop()
		elif neigh[(heading-1)%4] != None: # if there is a path to the left
			path.append(current)
			heading = (heading - 1) % 4
			current = neigh[heading]
		elif neigh[heading] != None: # if there is a path straight ahead
			path.append(current)
			current = neigh[heading]
		elif neigh[(heading+1)%4] != None: # if there is one to the right
			path.append(current)
			heading = (heading + 1) % 4
			current = neigh[heading]
		else: # dead end
			current = path.pop()
			current.Neighbours[heading] = None
			headings.pop()
			heading = headings.pop()

		headings.append(heading)

		# print(current.Position) # uncomment to debug pathing

	path.append(current) # appends the final node (end)
	return path