#!/bin/bash -l

# dependencies
SCRIPTPATH="/home/ferrer/toxim"

#SBATCH --output $SCRIPTPATH/cluster/"$UID".out

# run
sh $SCRIPTPATH/process_dock.sh
