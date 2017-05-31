grep -l 'EXPDTA    X-RAY DIFFRACTION' data/protein/structure/*.pdb | awk -F '/' '{ gsub(/.pdb/,""); print toupper($4)}'
