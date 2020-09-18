#! /usr/bin/env python3

from fasta_iterator_class import FASTAReader
  
    
reader = FASTAReader(open('droYak2_seq.fa'))
kmers = {}

k = 11

for seq_id, sequence in reader:
    for i in range(0, len(sequence) - k + 1):
        kmer = sequence[i:i + k]
        kmers.setdefault(kmer, [])
        kmers[kmer].append(i)
        
        
reader2 = FASTAReader(open('subset.fa'))
kmers2 = {}

k = 11

for seq_id2, sequence2 in reader2:
    for i in range(0, len(sequence2) - k + 1):
        kmer2 = sequence2[i:i + k]
        kmers2.setdefault(kmer2, {})
        kmers2[kmer2].setdefault(seq_id2, [])
        kmers2[kmer2][seq_id2].append(i)

for key in kmers.keys():
    if key in kmers2.keys():
        for seq_id in kmers2[key]:
            print(seq_id, kmers2[key][seq_id], kmers[key], key)
            
            
if __name__ == "__main__":
    seqs = FASTAReader(sys.stdin)
    for seq_id, sequence in seqs:
        print("{}: {}".format(seq_id, sequence), file = sys.stdout)
          