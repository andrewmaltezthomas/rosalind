file_name = raw_input("Enter file name: ")
f = open(file_name, 'r')


i = 1
for line in f.readlines():
	if i % 2 == 0:
		print line
	i += 1



