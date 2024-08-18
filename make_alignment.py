import pandas as pd
from Bio import SeqIO


sequence = SeqIO.parse('sequence.fasta', 'fasta')
sequence = next(sequence)
sequence_text = str(sequence.seq)

uni_prot_identifier = sequence.id.split('|')[1]


found_proteins = []
df = pd.read_excel('Peptides.xlsx')
for index, row in df.iterrows():
    proteins = row['Proteins'].split(';')
    for protein in proteins:
        if protein == uni_prot_identifier:
            found_proteins.append(row['Sequence'])


corrected_proteins = []
for item in found_proteins:
    missing = sequence_text.index(item)
    corrected_proteins.append(missing*' '+item)



with open('result.txt', 'wt') as f:
    f.write(sequence_text + '\n')
    for item in corrected_proteins:
        f.write(item + '\n')
