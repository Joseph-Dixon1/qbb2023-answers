1.1 

Rscript runChicago.R --design-dir raw/Design --en-feat-list raw/Features/featuresGM.txt --export-format washU_text raw/PCHIC_Data/GM_rep1.chinput,raw/PCHIC_Data/GM_rep2.chinput,raw/PCHIC_Data/GM_rep3.chinput output

1.2 

According to my output_feature_overlaps, significant interactions occur with CTCF, H3K4me1, H3K4me3, H3K27ac, and H3K9me3, but not in H3K27me3. These data mostly make sense to me, especially since CTCF is a cohesion complex that helps DNA form loop structures, which is why I would expect interactions at this point. Likewise, since these are likely promoter regions (target fragments), I'd expect associations with euchromatin markers such as H3K4me1, H3K4me3, and H3K27ac, but not H3K27me3 nor H3K9me3 since these are heterochromatin markers. Although the overlap was not associated with H3K27me3 as expected, it was surprising to see H3K9me3 overlap. 

2.2

two promoters
 chrom chromStart  chromEnd name score value ex color sourceChrom sourceStart sourceEnd             sourceName sourceStrand targetChrom targetStart targetEnd             targetName targetStrand
3074  chr21   31536992  32007984    .   143  5.21  .     0       chr21    32007037  32007984              KRTAP20-2            +       chr21    31536992  31543638                 CLDN17            +
3033  chr21   31656926  31991592    .   143  5.65  .     0       chr21    31656926  31663465              KRTAP25-1            +       chr21    31987530  31991592              KRTAP20-1            +
1169  chr20   35232257  35420209    .   143  5.63  .     0       chr20    35401729  35420209                   DSN1            +       chr20    35232257  35237961  C20orf24;RP5-977B1.11            +
1164  chr20   35232257  35275600    .   143  5.79  .     0       chr20    35272753  35275600                   SLA2            +       chr20    35232257  35237961  C20orf24;RP5-977B1.11            +
3035  chr21   31706561  31991592    .   143  5.74  .     0       chr21    31706561  31717256              KRTAP27-1            +       chr21    31987530  31991592              KRTAP20-1            +
1154  chr20   34821819  35237961    .   143  5.12  .     0       chr20    35232257  35237961  C20orf24;RP5-977B1.11            +       chr20    34821819  34830984                   AAR2            +


Promoter/Enhancer 
    chrom chromStart  chromEnd name score value ex color  ... sourceEnd sourceName sourceStrand targetChrom targetStart targetEnd targetName targetStrand
1     chr20      73978    170741    .   143  5.19  .     0  ...    170741    DEFB128            +       chr20       73978     76092          .            -
2700  chr21   15754564  16240999    .   143   5.2  .     0  ...  15761885     HSPA13            +       chr21    16237087  16240999          .            -
2701  chr21   15754564  16856803    .   143  5.58  .     0  ...  15761885     HSPA13            +       chr21    16849494  16856803          .            -
2702  chr21   15754564  16904789    .   143  5.73  .     0  ...  15761885     HSPA13            +       chr21    16901194  16904789          .            -
1224  chr20   36193496  36535161    .   143  5.52  .     0  ...  36535161     VSTM2L            +       chr20    36193496  36204066          .            -
1223  chr20   36183524  36535161    .   143   5.7  .     0  ...  36535161     VSTM2L            +       chr20    36183524  36184440          .            -


2.3
For VTSML, yes it's a transmembrane domain enabling cell-cell adhesion, and a negative regulator of apoptosis which means it's likely constitutively expressed. For DEFB128
For DEFB128, yes it's important for coding Defensins important for the immune response, which also likely needs to be expressed at high levels. 