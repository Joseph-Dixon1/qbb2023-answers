#!/bin/bash 

#1.1 

bwa index sacCer3.fa 

##1.2 

for sample in A01_09 A01_11 A01_23 A01_24 A01_27 A01_31 A01_35 A01_39 A01_62 A01_63 
do
	echo "Aligning sample: " ${sample} 
	bwa mem -t 4 -R "@RG\tID:${sample}\tSM:${sample}"\
	 sacCer3.fa \
	${sample}.fastq > ${sample}.sam
done

##1.3 

for file in A01_09 A01_11 A01_23 A01_24 A01_27 A01_31 A01_35 A01_39 A01_62 A01_63 
do
	echo 'sam files:' ${file}
	samtools sort ${file}.sam -O bam -o ${file}.bam
	samtools index ${file}.bam -M -o ${file}.bam.bai
done

#2.1 

###
bamfiles=('A01_09.fastq.bam','A01_11.fastq.bam','A01_23.fastq.bam','A01_24.fastq.bam','A01_27.fastq.bam','A01_31.fastq.bam','A01_35.fastq.bam','A01_39.fastq.bam','A01_62.fastq.bam','A01_63.fastq.bam')
freebayes -f sacCer3.fa --genotype-qualities -L A01_09.fastq.bam A01_11.fastq.bam A01_23.fastq.bam A01_24.fastq.bam A01_27.fastq.bam A01_31.fastq.bam A01_35.fastq.bam A01_39.fastq.bam A01_62.fastq.bam A01_63.fastq.bam > allvar.vcf
samtools view -H A01_09.fastq.bam | grep '^@RG' > read_groups.txt
freebayes -f sacCer3.fa --genotype-qualities --bam-list bam_list.txt --read-snp-limit read_groups.txt > allvar.vcf
samtools faidx sacCer3.fa
while read -r bam; do
    samtools quickcheck "$bam"
done < bam_list.txtf
ls *.bam > bam_list.txt
while read -r bam; do
    samtools sort -o "${bam%.bam}.sorted.bam" "$bam"
    samtools index "${bam%.bam}.sorted.bam"
done < bam_list.txt
freebayes -p 1 -f sacCer3.fa --genotype-qualities -L bam_list.txt > allvar.vcf

reference_genome="sacCer3.fa"

samtools view -H "${reference_genome}" > temporary_header.sam

while read -r bam; do
    samtools reheader temporary_header.sam "${bam}" > "${bam%.bam}_reheadered.bam"
done < bam_list.txt

ls *_reheadered.bam > bam_list.txt
freebayes -p 1 -f "${reference_genome}" --genotype-qualities -L bam_list.txt > allvar.vcf

ls *.fastq_reheadered.bam > bam_list.txt
freebayes -f sacCer3.fa --genotype-qualities -L bam_list.txt > allvar.vcf
####

ls *.bam > bam_list
freebayes -p 1 -f sacCer3.fa --genotype-qualities -L bam_list > allvar.vcf

#2.2 

vcffilter allvar.vcf -f "QUAL > 20" > filteredvariants.vcf

# #2.3 

vcfallelicprimitives filteredvariants.vcf -k -g > decomposed.vcf

#2.4 

snpEff download R64-1-1.105
snpEff ann R64-1-1.105 decomposed.vcf > annotated_variants.vcf 

head -n 100 annotated_variants.vcf > first100annotatedvariants.vcf
