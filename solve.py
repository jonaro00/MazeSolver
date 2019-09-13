from PIL import Image # pip install Pillow
import time
from maze import Maze

#from leftturn import solve
#from lefttorighttrun import solve
from leftturnonly import solve

def main():
	time_start = time.time()
	image = "mazes/perfect10k.png"
	print('Image:', image)
	im = Image.open(image)

	print("Creating maze")
	t0 = time.time()
	maze = Maze(im)
	t1 = time.time()
	time_diff = t1 - t0
	print("Time elapsed:", time_diff)

	print("Nodes:", len(maze.Nodes))
	
	print("Solving maze")
	t0 = time.time()
	result = solve(maze)
	t1 = time.time()
	time_diff = t1 - t0
	print("Time elapsed:", time_diff)
	result_length = len(result)
	print("Path length:", result_length)

	print("Saving image")
	im = im.convert('RGB')
	impixels = im.load()

	resultpath = [n.Position for n in result]

	for i in range(result_length - 1):
		a = resultpath[i]
		b = resultpath[i+1]

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