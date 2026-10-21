# BLAST XML Parsing with Biopython

A small learning project where I parse a BLAST result file (XML format) using Python and Biopython.

## What it does

- Reads `blast_result.xml` (BLASTP output for an insulin protein query)
- Counts the total number of alignments (hits)
- Selects a single hit and prints its title, length and accession
- Extracts the first HSP (High-scoring Segment Pair) of that hit and prints:
  - score and E-value
  - query range and subject range
  - query, matched and aligned sequences

## Requirements

- Python 3
- Biopython

```bash
pip install biopython
```

## Usage

Run the script from the folder that contains `blast_result.xml`:

```bash
cd SEQUENCE
python3 lesson13.py
```

## Example

```python
from Bio.Blast import NCBIXML

with open("blast_result.xml") as b:
    blast_record = NCBIXML.read(b)

print(len(blast_record.alignments))
```

## Notes

- Python indexing starts at 0, so Hit_num 10 in the XML is `alignments[9]`.
- BLAST positions are 1-based, while Python slicing is 0-based.

## Author

Hammad Memon, microbiologist learning bioinformatics (Python, Linux, R).
