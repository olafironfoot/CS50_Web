def square(x):
    return x * x

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		
p = Point(3, 5)

def main():
	for i in range(10):
	    print("{} squared is {}".format(i, square(i)))
if __name__ == '__main__':
	main()

