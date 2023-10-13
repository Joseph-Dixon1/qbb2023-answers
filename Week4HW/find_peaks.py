#!/usr/bin/env python

import sys

from Week4 import load_bedgraph, bin_array
import numpy as np 
import scipy.stats
import matplotlib.pyplot as plts


def main():
    # Load file names and fragment width
    forward_fname, reverse_fname, out_fname, control_forward, control_reverse, fragment_width = sys.argv[1:7]
    fragment_width=int(fragment_width)
    # Define what genomic region we want to analyze
    chrom = "chr2R"
    chromstart = 10000000
    chromend =  12000000
    chromlen = chromend - chromstart

    # Load the sample bedgraph data, reusing the function we already wrote
    forward = load_bedgraph(forward_fname, chrom, chromstart, chromend)
    reverse = load_bedgraph(reverse_fname, chrom, chromstart, chromend)

    # Combine tag densities, shifting by our previously found fragment width
    # fragmnet width adjustment
    sample=np.zeros(chromlen, int) # array saved in sample 
    sample[:-fragment_width//2] = reverse[fragment_width//2:] # // is a floor divide that gets rid of decimals 
    sample[fragment_width//2:] += forward[:-fragment_width//2] 

    # Load the control bedgraph data, reusing the function we already wrote
    forward_control = load_bedgraph(control_forward, chrom, chromstart, chromend)
    reverse_control = load_bedgraph(control_reverse,chrom, chromstart, chromend )

    # Combine tag densities
    combined_control=forward_control + reverse_control
    # Adjust the control to have the same coverage as our sample
    coverage_normal= np.sum(sample)/np.sum(combined_control)  # calculate total data in sample 
    combined_control=combined_control*coverage_normal

    # Create a background mean using our previous binning function and a 1K window
    # Make sure to adjust to be the mean expected per base ( we are scoring here)
    background_mean=bin_array(combined_control, 1000)
    background_mean=background_mean/1000

    # Find the mean tags ( mean reads /bp ( mean of control)) /bp and make each background position the higher of the
    # the binned score and global background score
    background_mean=np.maximum(background_mean, np.mean(combined_control)) # if background mean lower than global, bring it up to not get false positives


    # Score the sample using a binsize that is twice our fragment size
    # We can reuse the binning function we already wrote
    sample_scored=bin_array(sample, 2*fragment_width)

    # Find the p-value for each position (you can pass a whole array of values
    # and and array of means). Use scipy.stats.poisson for the distribution.
    # Remeber that we're looking for the probability of seeing a value this large
    # or larger
    # Also, don't forget that your background is per base, while your sample is
    # per 2 * width bases. You'll need to adjust your background
    pvalues= 1 - (scipy.stats.poisson.cdf(sample_scored, background_mean*2*fragment_width)) #calculate the p-value 

    # Transform the p-values into -log10
    # You will also need to set a minimum pvalue so you doen't get a divide by
    # zero error. I suggest using 1e-250
    pvalues=np.maximum(1e-250, pvalues)
    pvalues=-np.log10(pvalues)



    # Write p-values to a wiggle file. Write the output file, currently named x. 
    # The file should start with the line
    # "fixedStep chrom=CHROM start=CHROMSTART step=1 span=1" where CHROM and
    # CHROMSTART are filled in from your target genomic region. Then you have
    # one value per line (in this case, representing a value for each basepair).
    # Note that wiggle files start coordinates at 1, not zero, so add 1 to your
    # chromstart. Also, the file should end in the suffix ".wig"

    # Write bed file with non-overlapping peaks defined by high-scoring regions 

    write_wiggle(pvalues,chrom,chromstart,'ImTired2.wig')
    write_bed(pvalues, chrom, chromstart,chromend, fragment_width,'sample2_peaks.bed')

def write_wiggle(pvalues, chrom, chromstart, fnamwc e):
    output = open(fname, 'w')
    print(f"fixedStep chrom={chrom} start={chromstart + 1} step=1 span=1",
          file=output)
    for i in pvalues:
        print(i, file=output)
    output.close()

def write_bed(scores, chrom, chromstart, chromend, width, fname):
    chromlen = chromend - chromstart
    output = open(fname, 'w')
    while np.amax(scores) >= 10:
        pos = np.argmax(scores)
        start = pos
        while start > 0 and scores[start - 1] >= 10:
            start -= 1
        end = pos
        while end < chromlen - 1 and scores[end + 1] >= 10:
            end += 1
        end = min(chromlen, end + width - 1)
        print(f"{chrom}\t{start + chromstart}\t{end + chromstart}", file=output)
        scores[start:end] = 0
    output.close()


if __name__ == "__main__":
    main()


# Exercise 2 
#Question answered in README 

#Exercise 3 

