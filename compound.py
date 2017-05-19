import sys
from valid import Domain
import pubchempy

class Compound(Domain):

	NAME = 0
	FORMULA = 1
	WEIGHT = 2
	XLOGP = 3
	ROTB = 4
	HB_DONOR_N = 5
	HB_ACCEPTOR_N = 6
	HEAVY_ATOM_N = 7
	SYNONYM = 8
	ISO_SMILE = 9
	INCHI = 10

	def __init__(self,name):
		Domain.__init__(self, name)

	def fetchDrug(self, cid):
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

	def importData(self, source, savefreq):
		count = 0
		for cid in open(source):
			cid = cid.strip('\n')
			if self.idExists(cid):
				print(cid)
				continue

			drug = self.fetchDrug(cid)

			if self.addEntity(
				cid,
				{ (self.NAME, drug['name']),
				(self.FORMULA, drug['formula']),
				(self.WEIGHT, drug['weight']),
				(self.XLOGP, drug['xlogp']),
				(self.ROTB, drug['rotb']),
				(self.HB_DONOR_N, drug['hb_donor']),
				(self.HB_ACCEPTOR_N, drug['hb_acceptor']),
				(self.HEAVY_ATOM_N, drug['heavy_atom']),
				(self.SYNONYM, drug['synonym']),
				(self.ISO_SMILE,drug['iso_smile']),
				(self.INCHI, drug['inchi'])}
				):

				print(cid)

				count = (count + 1) % savefreq
				if count == 0:
					self.commit()

		if count < savefreq:
			self.commit()


	def listAll(self, sink):
		Domain.foreach(
			self, 
			lambda data: sink( (data[-1][1],data[0][1],data[1][1]) ),
			'e.dimension in (1,3)'
			)
