class Maze(object):

	class Node(object):
		def __init__(self, x, y):
			self.Position = (x, y)
			self.Neighbours = [None, None, None, None]


	def __init__(self, im):
		width = im.width
		height = im.height
		data = list(im.getdata(0))
		grid = [data[i*width:i*width+width] for i in range(height)]
		del data

		self.Nodes = [] 
		active_cols = [False] * width
		row_active = False

		left_node = None
		top_nodes = [None] * width

		for j, v in enumerate(grid[0]): # first row
			if v > 0:
				self.add_node(j,0)
				top_nodes[j] = self.Nodes[-1]
				active_cols[j] = True
				break

		for i, row in enumerate(grid[:-1]): # all rows between
			if i == 0: # start row has already been done, this is kept in the loop to keep the correct row index
				continue
			row_active = False
			left_node = None # reset before every row to prevent west-east links between rows
			for j, cell in enumerate(row):

				if j == 0: continue
				elif j == width - 1: continue

				add_this = False
				connect_west = False
				connect_north = False

				if cell > 0: # if white

					if active_cols[j]:      # if col is active
						if grid[i+1][j] == 0: # and if black below
							add_this = True
							active_cols[j] = False
						connect_north = True

					elif grid[i+1][j] > 0: # if white below
						add_this = True
						active_cols[j] = True
						connect_north = True

					if row_active:          # if row is active
						if grid[i][j+1] == 0: # and if black to the right
							add_this = True
							row_active = False
						connect_west = True

					elif grid[i][j+1] > 0: # if white to the right
						add_this = True
						row_active = True
						connect_west = True

					if active_cols[j] and row_active:
						add_this = True

					if add_this:
						self.add_node(j,i)

						newest_node = self.Nodes[-1]

						if connect_north:
							if top_nodes[j] != None:
								newest_node.Neighbours[0] = top_nodes[j]
								top_nodes[j].Neighbours[2] = newest_node
							top_nodes[j] = newest_node

						if connect_west:
							if left_node != None:
								newest_node.Neighbours[3] = left_node
								left_node.Neighbours[1] = newest_node
							left_node = newest_node

				else: # black
					left_node = None
					top_nodes[j] = None

		for j, v in enumerate(grid[-1]): # last row
			if v > 0:
				self.add_node(j,len(grid)-1)
				newest_node = self.Nodes[-1]
				newest_node.Neighbours[0] = top_nodes[j]
				top_nodes[j].Neighbours[2] = newest_node
				top_nodes[j] = newest_node
				break
		

		self.width = width
		self.height = height
		self.start = self.Nodes[0]
		self.end = self.Nodes[-1]

	def add_node(self, x, y):
		self.Nodes.append(Maze.Node(x,y))
		# print('Size of Nodes: ', self.Nodes.__sizeof__())
