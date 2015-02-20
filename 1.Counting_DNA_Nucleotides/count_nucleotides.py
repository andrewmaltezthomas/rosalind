#Open File
sequence = open("sequence_file.txt", 'r')
sequence_file = sequence.read()
print sequence_file

#Count nucleotides
adenines = sequence_file.count("A")
citosines = sequence_file.count("C")
timidines = sequence_file.count("T")
guanines = sequence_file.count("G")
print "A =",adenines,"C =",citosines,"G =",guanines,"T =",timidines




	

