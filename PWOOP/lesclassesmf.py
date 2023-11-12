
# encoding=utf-8

class film:
	def __init__(self, realisateur, nom):
		self.nom = nom
		self.realisateur = realisateur

	def set_nom(nom):
		self.nom = nom
	def get_nom(self):
		return self.nom


	def set_real(real):
		self.realisateur= real
	def get_real(self):
		return self.realisateur





class Personne:
	def __init__(self,nom,anne_naissance, lieu_naissance):
		self.nom = nom
		self.anne_naissance = anne_naissance
		self.lieu_naissance = lieu_naissance
	def set_nom(n_nom):
		self.nom = n_nom
	def get_nom(self):
		return self.nom
	def set_anne_naissance(anne_naissance):
		self.anne_naissance = anne_naissance
	def get_anne_naissance(self):
		return self.anne_naissance
	def set_lieu_de_naissance(lieu_naissance):
		self.lieu_naissance = lieu_naissance
	def get_lieu_de_naissance(self):
		return self.lieu_naissance


moi = Personne('Pierre-Antoine', "2006", "Paris")
acteur = Personne("Jean Pèche", "1986", "Les Anges")
realisateur = Personne("Alan Smithee", "1910", "Les Saints Bois")

print(realisateur.get_anne_naissance())