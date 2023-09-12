


def verifie(tab):
    sorted_tab = sorted(tab)
    if tab == sorted_tab:
        return True
    else:
        return False



def depouille(urne):
    resultat = {}
    for bulletin in urne:
        if bulletin in resultat:
            resultat[bulletin] = resultat[bulletin] + 1
        else:
            resultat[bulletin] = 1
    return resultat
def vainqueur(election):
    vainqueur = ''
    nmax = 0
    for candidat in election.values():
        if candidat > nmax:
            nmax = candidat
            vainqueur = candidat
    liste_finale = [nom for nom in election if election[nom] == vainqueur]
    return liste_finale


election = depouille(["A", "A", "B", "N", "B", "B", "N", "B"])
print(election)
print(vainqueur(election))