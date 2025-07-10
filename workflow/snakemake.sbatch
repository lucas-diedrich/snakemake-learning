#!/usr/bin/bash 

#SBATCH -J snakemake-test
#SBATCH --mem 16G
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH -o ./%j.out
#SBATCH -e ./%j.err

conda activate snakemake-env
conda config --remove channels defaults
conda config --add channels conda-forge
conda config --set channel_priority strict

snakemake --executor slurm \
    --default-resources \
    --jobs 3 \
    --use-conda
