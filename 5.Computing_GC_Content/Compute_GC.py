x = raw_input("Enter sequence file name: ")
f = open(x, 'r')
raw_samples = f.readlines()
f.close()

sequence = {}
sequence_id = ''

for elem in raw_samples:
    if elem[0] == '>':
        sequence_id = elem[1:].rstrip()
        sequence[sequence_id] = ''
    else:
        sequence[sequence_id] += elem.rstrip()

for s_id, s in sequence.iteritems():
    sequence[s_id] = (float(s.count('G') + s.count('C'))/len(s))*100

(s_id, gc) = max(list(sequence.iteritems()), key = lambda item:item[1])
print s_id
print str(gc) + "%"