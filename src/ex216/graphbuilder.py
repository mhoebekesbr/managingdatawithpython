import csv
import networkx


class GraphBuiler :

    def __init__(self):
        self.graph=networkx.Graph()


    def getGraph(self):
        return self.graph

    def buildGraphFromCsv(self, filename, srccolumn, destcolumn):
        self.graph=networkx.DiGraph()
        with open(filename) as infile :
            reader=csv.DictReader(infile,delimiter=';')
            for record in reader :
                src=record[srccolumn]
                dest=record[destcolumn]
                if not self.graph.has_edge(src,dest) :
                    self.graph.add_edge(src,dest)
                    self.graph[src][dest]['info']=[]
                edgeinfo={}
                for key in record.keys() :
                    if key not in (srccolumn,destcolumn) :
                        edgeinfo[key]=record[key]
                self.graph[src][dest]['info'].append(edgeinfo)

    def extractSubGraphWithSourceNode(self,srcnode):
        res=networkx.DiGraph()
        for (src,dest) in self.graph.edges() :
            if src == srcnode :
                res.add_edge(src,dest)
                res[src][dest]['info']=self.graph[src][dest]['info'][0]
        return res




