import re
import sys

handle = open(sys.argv[1])
lines = handle.readlines()

s1 = lines[1]
s1 = s1.rstrip()

introns = list() 

for line in lines[2:]:
	line = line.rstrip()
	if line.startswith(">"):
		continue
	introns.append(line)

codon_table = {"TTT": "F", "TTC": "F", "TTA": "L", "TTG": "L", "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S", "TAT": "Y", "TAC": "Y", "TAA": "Stop", "TAG": "Stop", "TGT": "C", "TGC": "C", "TGA": "Stop", "TGG": "W", "CTT" : "L", "CTC" : "L", "CTA" : "L", "CTG" : "L", "CCT" : "P", "CCC" : "P", "CCA" : "P", "CCG" : "P", "CAT" : "H", "CAC" : "H", "CAA" : "Q", "CAG" : "Q", "CGT" : "R", "CGC" : "R", "CGA" : "R", "CGG" : "R", "ATT" : "I", "ATC" : "I", "ATA" : "I", "ATG" : "M", "ACT" : "T", "ACC" :"T", "ACA" : "T", "ACG" : "T", "AAT" : "N", "AAC" : "N", "AAA" : "K", "AAG" : "K", "AGT" : "S", "AGC" : "S", "AGA" : "R", "AGG" : "R", "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V", "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A", "GAT": "D", "GAC": "D", "GAA": "E", "GAG": "E", "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G"} 
protein = []

for i in introns:
	s1 = re.sub(i, "", s1)

for i in range(0, len(s1), 3):
   	protein.append(codon_table[s1[i:i+3]])

print ''.join(protein[:-1])

handle.close()