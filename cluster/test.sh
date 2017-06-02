#!/bin/bash -l

# dependencies
#SCRIPTPATH="/home/ferrer/toxim/cluster"

# run
python test.py
#python $SCRIPTPATH/remove_line.py

rm slurm*.out

