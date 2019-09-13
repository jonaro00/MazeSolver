from collections import deque


def solve(maze):
	current = maze.start
	end = maze.end
	heading = 2
	path = deque([])

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

	path.append(current) # appends the final node (end)
	return path