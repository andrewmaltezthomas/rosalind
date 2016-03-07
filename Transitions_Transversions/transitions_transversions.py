import itertools

s1 = raw_input("Enter Sequence 1: ")
s2 = raw_input("Enter Sequence 2: ")

transversion = 0
transition = 0

for a, b in itertools.izip(s1, s2):
	if a != b:
		if (a == "A" and b == "G") or (b == "A" and a == "G") or (a == "C" and b == "T") or (b == "C" and a == "T"):
			transition += 1.0
		if (a == "A" or a == "G") and (b == "T" or b == "C") or (b == "A" or b == "G") and (a == "T" or a == "C"):
			transversion += 1.0

print transition/transversion
