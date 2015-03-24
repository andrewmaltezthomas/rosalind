"""
What this script does:

Input: Two UniProt ID's corresponding to two protein strings sss and ttt.

Return: The maximum score of any local alignment of sss and ttt.

Using:

The BLOSUM62 scoring matrix.
Gap opening penalty of 10.
Gap extension penalty of 1.
"""

from Bio import Entrez
from Bio import SeqIO
import requests

UNIPROT_URL = "http://www.uniprot.org/uniprot/{0}.fasta"
IDs = raw_input("Enter GenBank IDs separated by space: ")
IDs = IDs.split(" ")
print IDs

for i, uniprot_id in enumerate(IDs):
	fasta = requests.get(UNIPROT_URL.format(uniprot_id)).text
	print fasta
        with open(uniprot_id + '.fasta', 'w') as f:
            f.write(fasta)


# Run this in the command line:

# water uniprot_id.fasta uniprot_id.fasta -gapopen 10 -gapextend 1 -outfile Alignment.water
# more Alignment.water

