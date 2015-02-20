import math
a = raw_input("Enter value for beginning slice: ")
a = int(a)
b = raw_input("Enter value for terminating slice: ")
b = int(b)
b = b + 1 
c = raw_input("Enter value for beginning slice: ")
c = int(c)
d = raw_input("Enter value for terminating slice: ")
d = int(d)
d = d + 1
text = raw_input("Enter text: ")
sliced_text = text[a:b] + " " + text[c:d]
print sliced_text