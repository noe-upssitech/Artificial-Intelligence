"""
module principal pour l'etape 3
"""

from projet.outils.GrapheDeLieux import GrapheDeLieux
from projet.etape3.UneSolution import UneSolution

# rajouter ensuite le import permettant d'utiliser les solvers choisis
# from solvers.... import ...
from projet.solvers.SolverHC import SolverHC as HC
from projet.solvers.SolverTabou import SolverTabou as Tabou

class Etape3 :
    """  classe pour realiser les tests de l'etape 3 du projet (suite tache 2) """ 


    #    tests
    #    ////////////////////////////////////////////
    """  methode de TESTS pour Etape3
    """ 
    if __name__ == '__main__':

        nb_tentatives = 100
                       
        #    tests sur Etape 3
        #    ///////////////////
        #    cas 1 : 10 villes de 0 à 9
        tg : GrapheDeLieux = GrapheDeLieux.loadGraph("Data/town10.txt",True) 
        tsp : UneSolution = UneSolution(tg) 
        print("======== Solver 1 pour 10 villes de 0 a 9 : \n")
        HC.hilClimbing(tsp, nb_tentatives)

        print("======== Solver 2 pour 10 villes de 0 a 9 : \n")
        Tabou.tabou(tsp, nb_tentatives)                              
                                   
        #    ///////////////////
        #    cas 2 : 26 villes de 0 à 25
        tg = GrapheDeLieux.loadGraph("Data/town30.txt",True) 
        tsp = UneSolution(tg) 
        print("======== Solver 1 pour 26 villes de 0 a 25 : \n")
        HC.hilClimbing(tsp, nb_tentatives)

        print("======== Solver 2 pour 26 villes de 0 a 25 : \n")
        Tabou.tabou(tsp, nb_tentatives)                              
                                   
                                   
                                   
        #    ///////////////////
        #    cas 3 : 150 villes 
        tg = GrapheDeLieux.loadGraph("Data/town150.txt",True) 
        tsp = UneSolution(tg) 
        print("======== Solver 1 pour 150 villes : \n")
        HC.hilClimbing(tsp, nb_tentatives)
                                 
        print("======== Solver 2 pour 150 villes : \n")
        Tabou.tabou(tsp, nb_tentatives)                              
                                   
                                   
                                   
        #    ///////////////////
        #    cas 4 : 1000 villes 
        tg = GrapheDeLieux.loadGraph("Data/town1000.txt",True) 
        tsp = UneSolution(tg) 
        print("======== Solver 1 pour 1000 villes : \n")
        HC.hilClimbing(tsp, nb_tentatives)
                                 
        print("======== Solver 2 pour 1000 villes : \n")
        Tabou.tabou(tsp, nb_tentatives)                              
                                   
    

