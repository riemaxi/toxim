Toxim automated pipeline
Purpose of Toxim
Automation of the docking of a list of compounds into a list of proteins.
The result is a score matrix C x P x S, where 

C: set of compounds
P: set of proteins
S: subset of real numbers representing the estimated energy binding of 
a compound into a protein

Instructions
The pipeline works best if conda is installed with python 3.6.x

some how run the following commands

#MGLTools on our environment
module load utilities

#Conda
module load miniconda/3

#Required by obabel
module load gcc/6.2.0

#Required to fetch chemical compounds
module load openbabel

#Fast lane to autodock scripts
export PATH=$PATH:/home/apps/MGLTools/1.5.6/MGLTools-1.5.6/MGLToolsPckgs/AutoDockTools/Utilities24/

The structure of the software
toxim
 setup.sh
 compound_xxx
 protein_xxx
 process_xxx
 matrix_xxx
 
 parameter.txt
 parameter.py
 valid.py

 +data
   +docking
    +protein
    +compound
    +CID_PID
     *.map
     scoring.log
   +protein
    +structure
   +compound
    +structure
     +optimized

 +import

The pipeline
- setup procedure
  sh setup.sh

- Import compounds into data/compound.db
  sh compound_import.sh

- Fetch the compound structures into data/compound
  sh compound_fetch.sh

- Convert the compound structures from sdf to pdb
  sh compound_sdf_2_pdb.sh

-  Some compounds come with just 2 coordinates, so they need to be optimized up to 3 coordinates
  sh compound_optimize.sh

- Prepare the proteins for docking
  sh process_prepare_protein.sh

- Preparethe compounds fot docking
  sh process_prepare_compound.sh



#pubchempy
conda install -c mcs07 pubchemp
