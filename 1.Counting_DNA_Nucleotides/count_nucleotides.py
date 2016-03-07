"""
What this script does:
Input: A DNA string s of length at most 1000 nt.
Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.
"""
#Open File
sequence = open("dna3.fasta", 'r')
sequence_file = sequence.read()
print sequence_file

#Count nucleotides
adenines = sequence_file.count("A")
citosines = sequence_file.count("C")
timidines = sequence_file.count("T")
guanines = sequence_file.count("G")
print "A =",adenines,"C =",citosines,"G =",guanines,"T =",timidines




	

