import sys
from parameter import Parameter

p = Parameter()

for tpl in sys.stdin:
	cid, dim, score = tpl.strip('\n').split('\t')

	print (cid, dim, score)
