def get_file(func):
	def wraps(*args, **kwargs):
		count = 0
		while count < 3:
			try:
				func(*args, **kwargs)
				print("{} is exected".format(func.__name__))
			except Exception as e:
				print(e)
				print("Error Occured")
				count += 1
			else:
				break
	return wraps


@get_file
def read_file(file_name):
	with open(file_name, "r") as f:
		data = f.read()
		print(data)

read_file('hack.txt')

