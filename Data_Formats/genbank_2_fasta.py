"""
What this script does:

Given: A collection of GenBank entry IDs.

Returns: The shortest of the strings associated with the IDs in FASTA format.
"""

from Bio import Entrez
from Bio import SeqIO
Entrez.email = "andrewmaltezthomas@gmail.com"
IDs = raw_input("Enter GenBank IDs separated by commas: ")
IDs_list = []
IDs = IDs.split(",")
for i in IDs:
	IDs_list.append(i)

print IDs_list

handle = Entrez.efetch(db="nucleotide", id=IDs_list, rettype="fasta")
records = list(SeqIO.parse(handle, "fasta"))
print
for i in range(len(records)):
	if len(records[i]) == min([len(record.seq) for record in records]):
			print ">" + records[i].description 
			print records[i].seq

