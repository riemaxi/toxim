from protein import Protein
from parameter import Parameter
import sys

p = Parameter()

prot = Protein(p._('protein.db'))
prot.foreach(
	lambda data: print(  '\t'.join([field[1] for field in  data[1:]]) ),
)
prot.close()
