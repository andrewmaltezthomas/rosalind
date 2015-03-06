"""
What this script does:
Input: A DNA string t having length at most 1000 nt.
Return: The transcribed RNA string of t.
"""

#Translate to RNA
sequence = open("sequence_file.txt", 'r')
sequence_file = sequence.read()
print sequence_file
uracil = {'T':'U'}
def translate(text, dic):
    for i, j in dic.iteritems():
        text = text.replace(i, j)
    return text

print translate(sequence_file,uracil)
