"""
module pour l'etape 1
"""
from projet.outils.GrapheDeLieux import GrapheDeLieux
from projet.solvers.SolverSAT import SolverSAT

class Etape1 :
    """
    classe pour realiser l'etape 1 du projet (tache 1) 
    """
    # attributs
    # //////////////////////////////////////////////
    g : GrapheDeLieux 
    """
    le graphe representant le monde 
    """
    base : list
    """
    la base de clauses representant le probleme. 
    C'est une liste de listes d'entiers, un entier par variable, 
    (positif si literal positif, negatif sinon). 
    Attention le 0 n'est pas autorise pour represente une variable
    maj par majBase
    """
    nbVariables : int 
    """
    le nb de variables utilisees pour representer le probleme 
    maj par majBase
    """
    
    # constructeur
    # //////////////////////////////////////////////
    def __init__ (self, fn : str, form : bool) :
        """
        constructeur
        
        :param fn: le nom du fichier dans lequel sont donnes les sommets et les aretes
        
        :param form: permet de distinguer entre les differents types de fichier 
         (pour ceux contenant des poids et des coordonnees, form est True ;
          pour les autres, form est False)   
        """
        self.g = GrapheDeLieux.loadGraph(fn,form)
        self.base = [] 
        self.nbVariables = 0        
    
    # methodes
    # //////////////////////////////////////////////
    def encode(self, numero_sommet, numero_couleur, negation=False) :
        """
            methode pour encoder nos variables sous la forme d'entier numero_sommetnumero_couleur
            numero_sommet de 1 à infini
            numero_couleur de 1 à 99
        """
        if negation == False  :
            return numero_sommet*100 + numero_couleur
        if negation == True  :
            return -(numero_sommet*100 + numero_couleur)

    def decode(self,sommet_encode):
        """
            methode pour decoder nos variables sous la forme d'un string numero_sommet-numero_couleur pour un affichage plus clair
        """
        sommet_decode = [nombre for nombre in str(sommet_encode)]
        sommet_decode = sommet_decode[:2] + ['-'] + sommet_decode[2:]

        return "sommet : " + ''.join(sommet_decode)

    def majBase(self, nombre_couleurs : int) :
        """
        methode de maj de la base de clauses et du nb de variables en fonction du pb traite 
        param x: parametre servant pour definir la base qui representera le probleme 
        """
        def clause_couleurs(sommet):
            clause = []
            clause.append([self.encode(sommet, couleur) for couleur in range(1, nombre_couleurs + 1)])
            for couleur in range(1, nombre_couleurs + 1):
                couleur_suivante = couleur + 1 % nombre_couleurs
                clause.append([
                    self.encode(sommet, couleur, negation=True),
                    self.encode(sommet, couleur_suivante, negation=True)
                ])
            return clause

        def clause_adjacence(sommet):
            clause = []
            for couleur in range(1, nombre_couleurs + 1):
                for sommet_adjacent in self.g.getAdjacents(sommet):
                    clause.append([
                        self.encode(sommet, couleur, negation=True),
                        self.encode(sommet_adjacent, couleur, negation=True)
                    ])
            return clause

        self.base = []
        for sommet in self.g.getSommets():
            self.base += clause_couleurs(sommet)
            self.base += clause_adjacence(sommet)

        self.nbVariables = self.g.getNbSommets() * nombre_couleurs

    def execSolver(self) : 
        """
        methode d'appel du solver sur la base de clauses representant le pb traite
        
        :return True si la base de clauses representant le probleme est satisfiable, 
                False sinon
        """
        return SolverSAT.solve(self.base)     
    
    def affBase(self) :
        """
        affichage de la base de clauses representant le probleme 
        """
        print('Base de clause utilise ',self.nbVariables,' variables et contient les clauses suivantes : ') 
        for cl in self.base :
            print(cl) 
    

class __testEtape1__ : 
    """  
    methode principale de test
    """
    # TESTS
    # //////////////////////////////////////////////
    if __name__ == '__main__':
        
        # TEST 1 : town10.txt avec 3 couleurs
        print("Test sur fichier town10.txt avec 3 couleurs") 
        e = Etape1("Data/town10.txt",True) 
        e.majBase(3) 
        e.affBase()
        print("Resultat obtenu (on attend True) :",e.execSolver()) 
        
        # TEST 2 : town10.txt avec 2 couleurs
        print("Test sur fichier town10.txt avec 2 couleurs") 
        e.majBase(2) 
        #e.affBase() 
        print("Resultat obtenu (on attend False) :",e.execSolver()) 
    
        # TEST 3 : town10.txt avec 4 couleurs
        print("Test sur fichier town10.txt avec 4 couleurs") 
        e.majBase(4) 
        #e.affBase() 
        print("Resultat obtenu (on attend True) :",e.execSolver()) 
          
        # TEST 4 : flat20_3_0.col avec 4 couleurs
        print("Test sur fichier flat20_3_0.col avec 4 couleurs") 
        e = Etape1("Data/pb-etape1/flat20_3_0.col",False) 
        e.majBase(4) 
        # e.affBase() 
        print("Resultat obtenu (on attend True) :",e.execSolver()) 
        
        # TEST 5 : flat20_3_0.col avec 3 couleurs
        print("Test sur fichier flat20_3_0.col avec 3 couleurs") 
        e.majBase(3) 
        # e.affBase() 
        print("Resultat obtenu (on attend True) :",e.execSolver()) 
        
        # TEST 6 : flat20_3_0.col avec 2 couleurs
        print("Test sur fichier flat20_3_0.col avec 2 couleurs") 
        e.majBase(2) 
        # e.affBase() 
        print("Resultat obtenu (on attend False) :",e.execSolver()) 
        
        # TEST 7 : jean.col avec 10 couleurs
        print("Test sur fichier jean.col avec 10 couleurs") 
        e = Etape1("Data/pb-etape1/jean.col",False) 
        e.majBase(10) 
        # e.affBase() 
        print("Resultat obtenu (on attend True) :",e.execSolver()) 
        
        # TEST 9 : jean.col avec 9 couleurs
        print("Test sur fichier jean.col avec 9 couleurs") 
        e.majBase(9) 
        # e.affBase() 
        print("Resultat obtenu (on attend False) :",e.execSolver()) 
        
        # TEST 8 : jean.col avec 3 couleurs
        print("Test sur fichier jean.col avec 3 couleurs") 
        e.majBase(3) 
        # e.affBase() 
        print("Resultat obtenu (on attend False) :",e.execSolver()) 