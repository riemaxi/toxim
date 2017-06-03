grep -l 'EXPDTA' data/protein/structure/*.pdb | sort | awk -F '/' '{ gsub(/.pdb/,""); print toupper($4) "\t" NR-1}'
