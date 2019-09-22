#! /usr/bin/python3
from owlready2 import World, sync_reasoner


class SparqlQueries:
    def __init__(self):
        my_world = World()
        my_world.get_ontology("./Apsara_v3-1.owl").load() #path to the owl file is given here
        sync_reasoner(my_world)  #reasoner is started and synchronized here
        self._graph = my_world.as_rdflib_graph()

    def search(self):
        #Search query is given here
        #Base URL of your ontology has to be given here
        query = "PREFIX Apsara_v3: <http://www.semanticweb.org/dr-trange/ontologies/2019/8/Apsara_v3.owl#>" \
                "SELECT ?Apsara {" \
                "?Apsara Apsara_v3:hasBodyPosture Apsara_v3:Body_Picking_Flowers." \
                "}"

        #query is being run
        resultsList = self._graph.query(query)

        #creating json object
        response = resultsList
        for item in resultsList:
            print(str(item['Apsara'].toPython()).split('#')[1])
        return response
