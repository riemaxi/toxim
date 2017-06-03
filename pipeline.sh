#fetch compound data
sh compound_clone.sh

#import compounds
sh compound_import.sh

#prepare compounds
sh process_prepare_compound.sh

#import proteins out of  sergio's 
sh protein_import.sh

#fetch structures
sh process_fetch_protein_structure.sh

#init progress list. Used to recover from downtime
sh progress_init.sh

sh process_prepare_protein.sh

sh process_prepare_grid.sh
