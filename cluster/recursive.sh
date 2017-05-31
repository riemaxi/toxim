#!/bin/bash -l

# dependencies
SCRIPTPATH="/home/ferrer/toxim/cluster"

# run
python $SCRIPTPATH/remove_line.py

sbatch recursive.sh
