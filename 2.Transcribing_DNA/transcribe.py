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