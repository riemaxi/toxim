#!/bin/bash -l

#SBATCH --qos=high-throughput

# run
prepare_gpf4.py -l /home/ferrer/toxim/data/docking/protein/3EHS/molecule.pdbqt  -r protein.pdbqt -y -o protein.gpf

rm slurm*.out
touch prepare_grid.done

