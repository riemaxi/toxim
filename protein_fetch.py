import urllib.request as Ureq
import xml.etree.ElementTree
import sys
from parameter import Parameter

p = Parameter()

def records(ids, columns):
	url = 'http://www.rcsb.org/pdb/rest/customReport.xml?pdbids={0}&customReportColumns={1}&format=xml&service=wsfile'.format(ids, columns)
	req = Ureq.Request(url)

	doc = ''
	for chunck in Ureq.urlopen(req):
		doc += chunck.decode('utf8')
	return doc


def print_records(xmlrecords, columns):
	data = xml.etree.ElementTree.fromstring(xmlrecords)

	for record in data.findall('record'):
		fields = '\t'.join([record.find('dimStructure.' + name).text for name in columns.split(',')])
		print(fields)
	
columns = p._('protein.fetch.columns')
format = p._('protein.fetch.format')

for ids in sys.stdin:
	print_records(records(ids.strip('\n'), columns), columns)
