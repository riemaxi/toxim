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


def save(dir, cid, format, data):
	filename = '{}/{}.{}'.format(dir, cid, format)
	with open(filename,'w') as file:
		file.write(data)
	return filename


p = Parameter()

dir = p._('compound.fetch.structure')
format = p._('compound.fetch.format')

command = 'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{0}/{2}?record_type={1}d'
count = 0
for cid in sys.stdin:
	cid = cid.strip('\n')
	cdata = fetch(command.format(cid,3,format))
	if cdata:
		filename = save(dir, cid, format, cdata)

		count += 1
		print('{}\t{}\t{}'.format(count, cid,filename))
