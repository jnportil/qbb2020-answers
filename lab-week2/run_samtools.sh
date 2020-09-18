#!/bin/bash

for seq in 09 11 23 24 27 31 35 39 62 63
do
	samtools sort -O BAM -o srt_A01_${seq}.bam aln_A01_${seq}.sam 
done