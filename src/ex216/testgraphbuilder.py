import graphbuilder
import unittest

class GraphBuilderTest(unittest.TestCase) :


    def setUp(self):
        self.graphBuilder=graphbuilder.GraphBuiler()
        self.graphBuilder.buildGraphFromCsv('../../data/tabular/aquasymbio-data.csv','Symbiont accepted name','Host accepted name')

    def testBuildGraphFromCsv(self):
        graph=self.graphBuilder.getGraph()
        allnodes=list(graph.nodes())
        self.assertEqual(len(allnodes),1207)

    def testEdgeExists(self):
        graph=self.graphBuilder.getGraph()
        edge=graph['Parvilucifera infectans']['Alexandrium pacificum']
        self.assertIsNotNone(edge)

    def testEdgeHasInfo(self):
        graph=self.graphBuilder.getGraph()
        info=graph['Parvilucifera infectans']['Alexandrium pacificum']['info']
        self.assertEqual(len(info),2)

    def testExtractSubGraphWithSrcNode(self):
        subgraph=self.graphBuilder.extractSubGraphWithSourceNode('Amyloodinium ocellatum')
        allnodes=list(subgraph.nodes())
        self.assertEqual(len(allnodes),129)
