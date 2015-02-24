import re
print
sequence = raw_input("Enter sequence to search for motif: ")
motif = raw_input("Enter motif to search for: ")
motif_search = re.finditer('(?=%s)' % motif, sequence)
print
print "Found motif start in positions:"
print str([item.start(0)+1 for item in motif_search])
