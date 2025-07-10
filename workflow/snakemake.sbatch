#!/usr/bin/bash 

conda activate snakemake-env

snakemake --executor slurm \
    --default-resources \
    --jobs N 3 \
    --workflow-profile ./profiles/slurm 