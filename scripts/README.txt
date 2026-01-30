This folder contains general-purpose scripts for large-scale bacterial population genomics analyses.

Scripts are modular and can be used independently depending on study design.

Typical workflow order:

1. 01_quality_filtering.py        → Genome QC and filtering
2. 02_gene_cluster_detection.py   → Detection of genomic islands / loci
3. 03_annotation_prokka.sh        → Annotation of extracted contigs
4. 04_amr_detection.sh            → AMR gene screening
5. 05_plasmid_detection.sh        → Plasmid replicon detection
6. 06_phylogrouping.sh            → Phylogroup / MLST typing
7. 07_pangenome_panaroo.sh        → Pangenome reconstruction
8. 08_stat_analysis.R             → Statistical analysis & visualization

Note: These scripts represent a general workflow framework and do not include study-specific datasets or outputs.
