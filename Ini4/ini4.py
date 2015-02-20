a = raw_input("Enter value for a: ")
a = int(a)
b = raw_input("Enter valuer for b: ")
b = int(b) + 1
 

total = 0 
for n in range(a, b):
   if n % 2 == 1:
       total += n 

print total

