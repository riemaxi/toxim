import sys
from parameter import Parameter
import urllib.request as Ureq

def fetch(pid, dir):
	url = 'https://files.rcsb.org/download/{}.pdb'.format(pid)
	try:
		req = Ureq.Request(url)
		with Ureq.urlopen(req) as response:
			data = response.read().decode('utf8')

		open('{}/{}.pdb'.format(dir,pid),'w').write(data)
		return 1
	except:
		return 0
	

p = Parameter()

for pid in sys.stdin:
	pid = pid.strip('\n')
	if fetch(pid, p._('process.fetch_protein_structure.store_dir')):
		print(pid)
	else:
		print(pid,'?')
