# snakemake-learning
GitHub Repository for the hands-on snakemake learn session at the MannLabs Group Retreat 2025

Snakemake is a python-based workflow manager that is supposed to make your life easier when analysing large datasets. It **enforces reproducibility** and **enables scalability**. 

In this tutorial, we will 
1. read in a dataset
2. process it with a simple function
3. generate a plot as output
4. generate a report. 


## Installation 

1. Using the command line, go into your favorite directory (`cd /path/to/my/favorite/directory`)

2. Clone this repository 

```shell 
git clone https://github.com/lucas-diedrich/snakemake-learning.git
```

3. Go into the directory

```shell 
cd snakemake-learning
```

4. Create a `conda`/`mamba` environment with snakemake based on the `environemnt.yaml` file and activate it

```shell 
mamba create -n snakemake-env --file environment.yaml && mamba activate snakemake-env

# OR conda create -n snakemake-env --file environment.yaml && conda activate snakemake-env
```

5. Check if the installation was successful

```shell
snakemake --version
> 9.5.1
```


## Tutorial

Will be added soon...