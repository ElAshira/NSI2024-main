class Personne:
	def __init__(self, nom, sexe, adresse):
		self.nom=nom
		self.sexe = sexe
		self.adresse  = adresse

	def set_nom(self, rue):
		self.nom = nom
	def get_nom(self):
		return self.nom
	def set_sexe(self, rue):
		self.sexe = sexe
	def get_sexe(self):
		return self.sexe
	def set_adresse(self, rue):
		self.adresse = adresse
	def get_code_postale(self):
		return self.adresse
class Liste_personne:
	def __init__(self):
		self.tab = []
	def add_personne(self,persone):
		self.tab.append(persone)

	def find_nom(self,s):
		for i in self.tab:
			if i.get_nom() == s:
				return (i.get_nom(), i.get_sexe(), i.get_code_postale())
			else:
				pass

		return False

leandrounais = Personne("Leandre", "M", "La madeleine")
mathieunounais = Personne("Mathieu", "M", "Marcq")
liste_de_personne = Liste_personne()
liste_de_personne.add_personne(leandrounais)
liste_de_personne.add_personne(mathieunounais)
print(liste_de_personne.find_nom("Mathieu"))