from parameter import Parameter
import sys
import pubchempy

def fetchDrug(cid):
	drug = pubchempy.Compound.from_cid(cid)
	return {
		'name' : drug.iupac_name,
		'formula' : drug.molecular_formula,
		'weight' : drug.molecular_weight,
		'xlogp' : drug.xlogp,
		'rotb' : drug.rotatable_bond_count,
		'hb_donor' : drug.h_bond_donor_count,
		'hb_acceptor' :  drug.h_bond_acceptor_count,
		'heavy_atom' : drug.heavy_atom_count,
		'synonym' : drug.synonyms[0] if len(drug.synonyms) > 0 else '',
		'iso_smile' : drug.isomeric_smiles,
		'inchi' : drug.inchi
		}

HEADER = 'cid\tname\tformula\tweight\txlogp\trotb\thb_donor\thb_aceptor\theavy_atom\tsynonym\tiso_smile\tinchi\n'

p = Parameter()

freqsave = p.i('compound.freqsave')

out = open(p._('compound_clone.import'),'w')

count = 1
data = ''

out.write(HEADER)
for cid in sys.stdin:
	cid = cid.strip('\n')
	drug = fetchDrug(cid)
	data += '{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.\
		format(cid,drug['name'],drug['formula'],drug['weight'],
			drug['xlogp'],drug['rotb'], drug['hb_donor'],
			drug['hb_acceptor'],drug['heavy_atom'],drug['synonym'],
			drug['iso_smile'],drug['inchi'])

	if count % freqsave == 0:
		out.write(data)
		data = ''

	count += 1

	print('{}\t{}'.format(count-1, cid))

out.write(data)
	
out.close()
