"""
What this script does:

Given: The UniProt ID of a protein.

Returns: A list of biological processes in which the protein is involved (biological processes are found in a subsection of the protein's "Gene Ontology" (GO) section).
"""

from Bio import ExPASy
from Bio import SwissProt

ID = raw_input("Enter UniProt ID for the protein: ")
handle = ExPASy.get_sprot_raw(ID)
record = SwissProt.read(handle)
print dir(record)
for i in record.cross_references:
  if (i[0] == 'GO'):
	if (i[2][0] == 'P'):
		print i[2][2:]
