#!/bin/bash -l

# run
prepare_gpf4.py -l /home/ferrer/toxim/data/docking/protein/5HYK/molecule.pdbqt  -r protein.pdbqt -y -o protein.gpf

rm slurm*.out

