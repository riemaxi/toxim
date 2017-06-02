#!/bin/bash -l

# run
prepare_gpf4.py -l {0}  -r protein.pdbqt -y -o protein.gpf

rm slurm*.out

