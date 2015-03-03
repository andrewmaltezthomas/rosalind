"""
What this script does:

Input: A genus name, followed by two dates in YYYY/M/D format.

Returns: The number of Nucleotide GenBank entries for the given genus that were published between the dates specified.
"""

from Bio import Entrez
Entrez.email = "andrewmaltezthomas@gmail.com"
organism = raw_input("Enter genus name for organism: ")
organism = organism + "[Organism]"
database = raw_input("Enter database to search for: ")
start_date = raw_input("Enter start date: ")
end_date = raw_input("Enter end date: ")
handle = Entrez.esearch(db=database, term=organism, datetype='pdat', mindate= start_date, maxdate=end_date)
record = Entrez.read(handle)
print record["Count"]
