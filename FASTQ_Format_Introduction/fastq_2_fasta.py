"""
What this script does:
Input: FASTQ file

Return: Corresponding FASTA records
"""
from Bio import SeqIO
sequence_file = raw_input("Enter sequence file name: ")
out_handle = open('Sequence.fasta', 'w')
SeqIO.convert(sequence_file, "fastq", out_handle, "fasta")
out_handle.close()


