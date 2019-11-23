from owlready2 import World, sync_reasoner


class SingletonSparkQL:
    _instance = None

    def __init__(self):
        """ Virtually private constructor. """
        if SingletonSparkQL._instance != None:
            raise Exception("This class is a singleton!")
        else:
            SingletonSparkQL._instance = self
    @staticmethod
    def getInstance():
        """ Static access method. """
        if SingletonSparkQL._instance == None:
            SingletonSparkQL._instance = SparqlQueries()
        return SingletonSparkQL._instance

class SparqlQueries ():
    def __init__(self):
        my_world = World()
        my_world.get_ontology("./query_dance/query/Apsara_v3-1.owl").load() #path to the owl file is given here
        sync_reasoner(my_world)  #reasoner is started and synchronized here
        self._graph = my_world.as_rdflib_graph()

    def search(self,q):
        #Search query is given here
        #Base URL of your ontology has to be given here
        query = "PREFIX Apsara_v3: <http://www.semanticweb.org/dr-trange/ontologies/2019/8/Apsara_v3.owl#>" \
                "SELECT ?Apsara { "+q+ "}"
        # query is being run
        print (query)
        resultsList = self._graph.query(query)
        #creating json object
        response = list()
        for item in resultsList:
            response.append(str(item['Apsara'].toPython()).split('#')[1])
        return response