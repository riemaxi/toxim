import urllib.request as Ureq
import sys
from parameter import Parameter

def fetch(url):
	try:
		req = Ureq.Request(url)
		with Ureq.urlopen(req) as response:
			data = response.read().decode('utf8')
		
		return data
	except:
		return 0

p = Parameter()
dir = p._('compound.fetch.structure')
format = p._('compound.fetch.format')

def save(dir, cid, xd, format, data):
	filename = '{0}/{1}_{2}.{3}'.format(dir, cid, xd, format)
	with open(filename,'w') as file:
		file.write(data)

command = 'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{0}/{2}?record_type={1}d'
count = 0
for cid in sys.stdin:
	cid = cid.strip('\n')
	print('{0}\t{1}'.format(count + 1, cid))
	cdata = fetch(command.format(cid,3,format))
	if cdata:
		save(dir, cid,'3d', format, cdata)
	else:
		cdata = fetch(command.format(cid,2, format))
		save(dir, cid,'2d', format, cdata)

	count += 1
