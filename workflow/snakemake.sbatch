#!/usr/bin/bash 

#SBATCH -J snakemake-test
#SBATCH --mem 16G
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH -o ./%j.out
#SBATCH -e ./%j.err


# Load anaconda
# This might be cluster-specific
module load anaconda/3/2023.03

# Set channel priorities and only use conda-forge
# This might be cluster-specific
conda config --remove channels defaults
conda config --add channels conda-forge
conda config --set channel_priority strict

# Activate the snakemake environment
conda activate snakemake-env

# Use the snakemake slurm executor
# --default-resources: Automatically determine the resources
# --jobs 100: Limit the number of concurrent jobs to 100 (unlimited for uncapped numbers)
# --use-conda: Use conda
snakemake --executor slurm \
    --default-resources \
    --jobs 3 \
    --use-conda
