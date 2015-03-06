"""
What this script does:

Given: Two GenBank IDs.

Return: The maximum global alignment score between the DNA strings associated with these IDs.

Using:
The DNAfull scoring matrix
Gap opening penalty of 10.
Gap extension penalty of 1.
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

handle_1 = Entrez.efetch(db="nucleotide", id=IDs_list[0], rettype="fasta")
records_1 = SeqIO.parse(handle_1, "fasta")
output_handle_1 = open('Sequence_1.fasta', 'w')
SeqIO.write(records_1, output_handle_1, "fasta")
output_handle_1.close()

handle_2 = Entrez.efetch(db="nucleotide", id=IDs_list[1], rettype="fasta")
records_2 = SeqIO.parse(handle_2, "fasta")
output_handle_2 = open('Sequence_2.fasta', 'w')
SeqIO.write(records_2, output_handle_2, "fasta")
output_handle_2.close()

# In the command line run:
# needle Sequence_1.fasta Sequence_2.fasta -gapopen 10 -gapextend 1 -endweight Y -endopen 10 -endextend 1 -outfile rosalind.needle
# more rosalind.needle


