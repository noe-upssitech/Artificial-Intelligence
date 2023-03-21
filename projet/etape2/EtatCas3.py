"""
module pour l'état de l'etape 2 ds le cas 3
"""
from projet.outils.GrapheDeLieux import GrapheDeLieux
from projet.etape2.Etat import Etat

class EtatCas3(Etat) :
    """ 
    Classe pour definir un etat pour le cas 3 de la tache 2
    """ 
    # attributs
    # A COMPLETER
    # //////////////////////////////////////////////
    tg : GrapheDeLieux
    """ le graphe representant le monde """ 
    
    # constructeurs
    # A ECRIRE/MODIFIER/COMPLETER
    # //////////////////////////////////////////////
    def __init__(self, tg : GrapheDeLieux, etat_courant: int=0, objectif: int=0, visite: list=[0]) :
        """ constructeur d'un etat a partir du graphe representant le monde
        
        :param tg: graphe representant le monde
        :param param1: a definir eventuellement
        :param param2: a definir eventuellement
        """ 
        self.tg = tg
        self.etat_courant = etat_courant
        self.objectif = objectif
        self.visite = visite
     
    
    # methodes issues de Etat
    # //////////////////////////////////////////////
    def estSolution(self) :
        """ methode detectant si l'etat est une solution
        
        :return true si l'etat courant est une solution, false sinon
        """ 
        # A ECRIRE et MODIFIER le return en consequence
        return (self.etat_courant == self.objectif) and (len(self.visite) == self.tg.getNbSommets() + 1) 
    
    
    def successeurs(self) :
        """ methode permettant de recuperer la liste des etats successeurs de l'etat courant
        
        :return liste des etats successeurs de l'etat courant
        """ 
        successeurs = self.tg.getSommets()
        sommets_gardes = []

        for sommet in successeurs:
            if sommet not in self.visite:
                sommets_gardes.append(sommet)
            elif len(self.visite) == self.tg.getNbSommets() and sommet == self.objectif:
                sommets_gardes.append(sommet)
        
        return [EtatCas3(tg=self.tg, etat_courant=sommet, objectif=self.objectif, visite=self.visite + [sommet]) for sommet in sommets_gardes]
    
    
    def h(self) :  
        """ methode permettant de recuperer l'heuristique de l'etat courant 
        
        :return heuristique de l'etat courant
        """ 
        # A ECRIRE et MODIFIER le return en consequence
        # Return la distance minimum restant à parcourir pour être passé par toutes les villes de la carte  
        return  self.tg.getPoidsMinAir() * (self.tg.getNbSommets() - len(self.visite))
    
    
    def k(self, e) :
        """ methode permettant de recuperer le cout du passage de l'etat courant à l'etat e
        
        :param e: un etat
        
        :return cout du passage de l'etat courant à l'etat e
        """ 
        # A ECRIRE et MODIFIER le return en consequence
        return GrapheDeLieux.dist(self.etat_courant, e.etat_courant, self.tg)
    
    
    def displayPath(self) :
        """ methode pour afficher le chemin qui a mene a l'etat courant en utilisant la map des peres
        
        :param pere: map donnant pour chaque etat, son pere 
        """ 
        print("resultat trouve : " + str(self.visite))
    
    
    
    # methodes pour pouvoir utiliser cet objet dans des listes et des map
    # //////////////////////////////////////////////
    def __hash__(self) :
        """ methode permettant de recuperer le code de hachage de l'etat courant
        pour une utilisation dans des tables de hachage
        
        :return code de hachage
        """ 
        # A ECRIRE et MODIFIER le return en consequence
        return ''.join([str(sommet) for sommet in self.visite]).__hash__()
    
    
    def __eq__(self, o) :
        """ methode de comparaison de l'etat courant avec l'objet o
        
        :param o: l'objet avec lequel on compare
        
        :return true si l'etat courant et o sont egaux, false sinon
        """ 
        # A ECRIRE et MODIFIER le return en consequence
        return self.etat_courant == o
    
    # methode pour affichage futur (heritee d'Object)
    # //////////////////////////////////////////////
    def __str__(self) : 
        """ methode mettant l'etat courant sous la forme d'une 
        chaine de caracteres en prevision d'un futur affichage
        
        :return representation de l'etat courant sour la forme d'une 
        chaine de caracteres
        """ 
        # A ECRIRE et MODIFIER le return en consequence
        return str(self.etat_courant)



