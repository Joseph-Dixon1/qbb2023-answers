1.1 
	plink --vcf genotypes.vcf --pca 

	to print top 10 principal components used: head -n 10 plink.eigenvec 

2.2 
	plink --vcf genotypes.vcf --make-bed --out genotypes_plink 
	plink --bfile genotypes_plink --freq --out allele_fr  



3.1 

	plink --vcf genotypes.vcf --linear --pheno phenotype.txt --covar pca.eigenvec --allow-no-sex --out phenotype_gwas_results


3.4
	 There's only one gene closest allegedly which is tubulin, encoding alpha tubulin, alpha tubulin is a subunit of the MT dimer tubulin, MT polymerization is an essential component of cell division during interphase and mitotic progression, therefore, no tub = disease. 