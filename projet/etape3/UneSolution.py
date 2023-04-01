"""  module pour la classe UneSolution """ 

from projet.outils.GrapheDeLieux import GrapheDeLieux
from projet.etape3.Solution import Solution

import random as rand

class UneSolution(Solution) :
    """  
    Classe pour definir une solution pour le cas 3 de la tache 2 (hérite de Solution)
    """ 
    
    
    #    attributs
    #    A COMPLETER
    #    //////////////////////////////////////////////
    tg : GrapheDeLieux
    """  le graphe representant le monde """ 
    
    #    constructeurs
    #    A ECRIRE/COMPLETER
    #    //////////////////////////////////////////////
    def __init__(self, tg : GrapheDeLieux, chemin: list=[0]) :
        """ constructeur d'un etat a partir du graphe representant le monde
        
        :param tg: graphe representant le monde
        :param param1: a definir eventuellement
        :param param2: a definir eventuellement
        """ 
        self.tg = tg
        self.chemin = chemin
        #self.rand = rand.Random()

        if len(self.chemin) == 0:
            self.chemin = self.nelleSolution().chemin
    
    
    #    methodes de la classe abstraite Solution
    #    //////////////////////////////////////////////
    def lesVoisins(self) :
        """  methode recuperant la liste des voisins de la solution courante
        
        :return liste des voisins de la solution courante
        """ 

        voisins = []
        nouveau_chemin = self.chemin[1:-1]
        print(f"self.chemin = {self.chemin}")
        print(f"nouveau_chemin = {nouveau_chemin}")

        for i in range(1, len(nouveau_chemin)):
            print("test")
            tmp = nouveau_chemin[i-1]
            nouveau_chemin[i-1] = nouveau_chemin[i]
            nouveau_chemin[i] = tmp
            voisins.append(UneSolution(self.tg, [0] + nouveau_chemin + [0]))

        return voisins
    
    

    def unVoisin(self) : 
        """  methode recuperant un voisin de la solution courante
        
        :return voisin de la solution courante
        """ 
        #    A ECRIRE et MAJ la valeur retournee

        voisins = self.lesVoisins()    
        #print(f"voisins = {voisins}")
    

        return [voisins[rand.randint(0, len(voisins)-1)]]
    

    def eval(self) : 
        """  methode recuperant la valeur de la solution courante
        
        :return valeur de la solution courante
        """ 
        #    A ECRIRE et MAJ la valeur retournee
        result = []
        for i in range(1, len(self.chemin)):
            result.append(GrapheDeLieux.dist(self.chemin[i-1], self.chemin[i], self.tg))
        
        return sum(result)
    
    
    def nelleSolution(self) : 
        """  methode generant aleatoirement une nouvelle solution 
        a partir de la solution courante
        
        :return nouvelle solution generee aleatoirement a partir de la solution courante
        """ 
        #    A ECRIRE et MAJ la valeur retournee
        chemin = list(range(1, self.tg.getNbSommets()))
        rand.shuffle(chemin)

        return UneSolution(self.tg, [0] + chemin + [0])
    
    
    def displayPath(self, pere) :
        """ methode pour afficher le chemin qui a mene a l'etat courant en utilisant la map des peres
        
        :param pere: map donnant pour chaque etat, son pere 
        """ 
        print("resultat trouve : " + str(self.visite))
    
    #    methodes pour pouvoir utiliser cet objet dans des listes et des map
    #    //////////////////////////////////////////////
    def __hash__(self) :
        """ methode permettant de recuperer le code de hachage de l'etat courant
        pour une utilisation dans des tables de hachage
        
        :return code de hachage
        """ 
        # A ECRIRE et MODIFIER le return en consequence
        return ''.join([str(sommet) for sommet in self.chemin]).__hash__()
    
    
    def __eq__(self, o) :
        """ methode de comparaison de l'etat courant avec l'objet o
        
        :param o: l'objet avec lequel on compare
        
        :return true si l'etat courant et o sont egaux, false sinon
        """ 
        # A ECRIRE et MODIFIER le return en consequence
        return self.chemin == o
    
    # methode pour affichage futur (heritee d'Object)
    # //////////////////////////////////////////////
    def __str__(self) : 
        """ methode mettant l'etat courant sous la forme d'une 
        chaine de caracteres en prevision d'un futur affichage
        
        :return representation de l'etat courant sour la forme d'une 
        chaine de caracteres
        """ 
        # A ECRIRE et MODIFIER le return en consequence
        return f"chemin = {self.chemin}, cout = {self.eval()} \n"
    


