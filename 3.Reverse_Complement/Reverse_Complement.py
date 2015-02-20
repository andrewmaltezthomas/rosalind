#Import Sequence File
import os
print
user_path = raw_input("Enter sequence file location: ")
path = os.chdir(user_path)
print
sequence_file_location = raw_input("Enter sequence file name: ")
print
sequence_file = open(sequence_file_location, "r")
sequence_file = sequence_file.read()

#Reverse the sequence
print
print "Sequence is:"
print
print sequence_file
sequence_file_reversed = sequence_file[::-1]
print "Reverse Sequence is:"
print sequence_file_reversed

#Complement the sequence
dic = {'A': 't', 'T': 'a', 'C': 'g', 'G': 'c', 'N': 'n', 'I': 'i', 'U': 'a', 'Y': 'r', 'R': 'y', 'K': 'm', 'M': 'k', 'B': 'v', 'D': 'h', 'H': 'd', 'V': 'b', 'S': 'w', 'W': 's'}
def complement(text, dic):
    #Complement
    for i, j in dic.iteritems():
        text = text.replace(i, j)
    text = text.upper()
    return text
sequence_file_rc = complement(sequence_file_reversed,dic)
print 
print "Reverse Complement Sequence is:"
print sequence_file_rc
print 


#ROSALIND SOLUTION
#input S 
#reverse S 
#for i = 1 to length of S 
#     if S[i] = 'A' then S'[i] = 'T'
#     if S[i] = 'T' then S'[i] = 'A'
#     if S[i] = 'C' then S'[i] = 'G'
#     if S[i] = 'G' then S'[i] = 'C'
#       
#
#print S'
