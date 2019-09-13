from PIL import Image # pip install Pillow
import time
from maze import Maze

from leftturnonly import solve as solve1
from rightturnonly import solve as solve2

def main():
	time_start = time.time()
	image = "mazes/perfect10k.png"
	print('Image:', image)
	im = Image.open(image)

	print("Creating maze 1")
	t0 = time.time()
	maze = Maze(im)
	t1 = time.time()
	time_diff = t1 - t0
	print("Time elapsed:", time_diff)

	print("Nodes:", len(maze.Nodes))
	
	print("Solving maze 1")
	t0 = time.time()
	result = solve1(maze)
	t1 = time.time()
	time_diff = t1 - t0
	print("Time elapsed:", time_diff)
	result_length = len(result)
	print("Path length:", result_length)

	maze.Nodes.clear() #del maze.Nodes[:]
	del maze

	print('Preparing image 2')
	result = [n.Position for n in result]
	
	im2 = Image.new(mode='P', size=(im.width, im.height))
	im2 = im2.convert('RGB')
	im2pixels = im2.load()

	for i in range(result_length - 1):
		a = result[i]
		b = result[i+1]
		px = (255, 255, 255)

		if a[1] == b[1]:
			for x in range(min(a[0],b[0]),max(a[0],b[0]) + 1):
				im2pixels[x,a[1]] = px
		elif a[0] == b[0]:
			for y in range(min(a[1],b[1]),max(a[1],b[1]) + 1):
				im2pixels[a[0],y] = px
	im2.save("temp.png")

	result.clear()

	print("Creating maze 2")
	t0 = time.time()
	maze = Maze(im2)
	t1 = time.time()
	time_diff = t1 - t0
	print("Time elapsed:", time_diff)

	print("Nodes:", len(maze.Nodes))
	
	print("Solving maze 2")
	t0 = time.time()
	result = solve2(maze)
	t1 = time.time()
	time_diff = t1 - t0
	print("Time elapsed:", time_diff)
	result_length = len(result)
	print("Path length:", result_length)

	result = [n.Position for n in result]

	im = im.convert('RGB')
	impixels = im.load()
	print("Saving image")

	for i in range(result_length - 1):
		a = result[i]
		b = result[i+1]

		r = int((i / result_length) * 255)
		px = (0, 255, 255 - r)

		if a[1] == b[1]:
			for x in range(min(a[0],b[0]),max(a[0],b[0]) + 1):
				impixels[x,a[1]] = px
		elif a[0] == b[0]:
			for y in range(min(a[1],b[1]),max(a[1],b[1]) + 1):
				impixels[a[0],y] = px

	im.save("solved.png")
	time_end = time.time()
	total_time = time_end - time_start
	print('Total time elapsed:', total_time)


if __name__ == "__main__":
	main()