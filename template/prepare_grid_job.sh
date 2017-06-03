#!/bin/bash -l

#SBATCH --qos=high-throughput

# run
prepare_gpf4.py -l {0}  -r protein.pdbqt -y -o protein.gpf

rm slurm*.out
touch prepare_grid.done

