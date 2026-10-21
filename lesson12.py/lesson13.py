from Bio.Blast import NCBIXML

with open("blast_result.xml") as b:
    blast_record = NCBIXML.read(b)

print(len(blast_record.alignments))

first_alignment = blast_record.alignments[28]
# print (first_alignment.title)
# print (first_alignment.length)

# print(len(first_alignment.hsps))

first_hsp = first_alignment.hsps[0]
 #print(first_hsp.score)
# print(first_hsp.expect)


 # print("Query sequence")  
# print(first_hsp.query)

# print("Matched seq")
# print(first_hsp.sbjct)

# print("Alignment seq")
# print(first_hsp.match)


print("Query range:", first_hsp.query_start, first_hsp.query_end)
print("Subject range:", first_hsp.sbjct_start, first_hsp.sbjct_end)


