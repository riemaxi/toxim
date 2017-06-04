#!/bin/bash -l

#SBATCH --qos=high-throughput

# run
autogrid4 -p protein.gpf

rm slurm*.out
touch create_grid.done
