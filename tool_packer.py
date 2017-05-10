import sys
from parameter import Parameter

p = Parameter()

payload = p.i('tool.packer.payload')
delim = p._('tool.packer.del')

count = 0
items = []
for item in sys.stdin:
	item = item.strip('\n')
	items.append(item)
	count = (count + 1) % payload
	if count == 0:
		print ('{}'.format(delim).join(items))
		items = []

if count < payload:
	print ('{}'.format(delim).join(items))
