#!/bin/bash

for seq in 09 11 23 24 27 31 35 39 62 63
do
	bwa mem -R "@RG\tID:${seq}\tSM:{seq}" -t -o  sacCer3.fa A01_${seq}.fastq > aln_A01_${seq}.sam
done