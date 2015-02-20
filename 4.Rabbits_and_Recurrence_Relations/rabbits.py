rabbits = raw_input("Enter number of rabbit pairs:")
rab = int(rabbits)
months = raw_input("Enter number of months:")
months = int(months)

fib_list = []
for i in range(months):
	if i < 2: 
		fib_list.append(1)
	else:
		fib_list.append(fib_list[-1] + fib_list[-2]*rab)
print fib_list[-1]

