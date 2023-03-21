"""
module pour l'état de l'etape 2 ds le cas 1
"""
from projet.outils.GrapheDeLieux import GrapheDeLieux
from projet.etape2.Etat import Etat
from projet.outils.Lieu import Lieu


class EtatCas1(Etat) :
    """ Classe pour definir un etat pour le cas 1 de la tache 2 (hérite de Etat)
    """ 
    
    # attributs
    # A COMPLETER
    # //////////////////////////////////////////////
    tg : GrapheDeLieux
    etat_courant : int
    objectif : int
    """ le graphe representant le monde """ 
    
    # constructeurs
    # A ECRIRE/MODIFIER/COMPLETER
    # //////////////////////////////////////////////
    def __init__(self, tg : GrapheDeLieux, etat_courant : int, objectif : int) :
        """ constructeur d'un etat a partir du graphe representant le monde
        
        :param tg: graphe representant le monde
        
        :param param1: a definir eventuellement
        
        :param param2: a definir eventuellement
        """ 
        self.tg = tg
        self.etat_courant = etat_courant
        self.objectif = objectif
        # a completer pour tenir compte de la presence ou pas des deux derniers parametres
    
    # methodes issues de Etat
    # //////////////////////////////////////////////
    def estSolution(self) :
        """ methode detectant si l'etat est une solution
        
        :return true si l'etat courant est une solution, false sinon
        """ 
        # A ECRIRE et MODIFIER le return en consequence
        return self.etat_courant == self.objectif
    
    def successeurs(self) :
        """ methode permettant de recuperer la liste des etats successeurs de l'etat courant
        
        :return liste des etats successeurs de l'etat courant
        """ 

        list_sommet = self.tg.getAdjacents(self.etat_courant)
        return [EtatCas1(self.tg, sommet, self.objectif) for sommet in list_sommet]
    
    def h(self) :  
        """ methode permettant de recuperer l'heuristique de l'etat courant 
        
        :return heuristique de l'etat courant
        """ 
        # A ECRIRE et MODIFIER le return en consequence
        return GrapheDeLieux.dist(self.etat_courant, self.objectif, self.tg)
    
    
    def k(self, e) :
        """ methode permettant de recuperer le cout du passage de l'etat courant à l'etat e
        
        :param e: un etat
        
        :return cout du passage de l'etat courant à l'etat e
        """ 
        # A ECRIRE et MODIFIER le return en consequence
        return self.tg.getCoutArete(self.etat_courant, e)
    
    
    def displayPath(self, pere) :
        """ methode pour afficher le chemin qui a mene a l'etat courant en utilisant la map des peres
        
        :param pere: map donnant pour chaque etat, son pere 
        """ 
        chemin = []
        etat = self
        while etat != None:
            chemin.append(etat.etat_courant)
            etat = pere[etat]

        print("resultat trouve : " + str(chemin))
    
    
    # methodes pour pouvoir utiliser cet objet dans des listes et des map
    # //////////////////////////////////////////////
    def __hash__(self) :
        """ methode permettant de recuperer le code de hachage de l'etat courant
        pour une utilisation dans des tables de hachage
        
        :return code de hachage
        """ 
        # A ECRIRE et MODIFIER le return en consequence
        return 0 
    
    
    def __eq__(self, o) :
        """ methode de comparaison de l'etat courant avec l'objet o
        
        :param o: l'objet avec lequel on compare
        
        :return true si l'etat courant et o sont egaux, false sinon
        """ 
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
    



