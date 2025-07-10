#!/usr/bin/bash 

#SBATCH -J snakemake-test
#SBATCH --mem 2G
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4

conda activate snakemake-env

snakemake --executor slurm \
    --default-resources \
    --jobs N 3 \
    --workflow-profile ./profiles/slurm 