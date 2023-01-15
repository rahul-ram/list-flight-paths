import unittest
import os
import json

from flight_paths import Graph


class TestFlightPaths(unittest.TestCase):

    def setUp(self):  # {
        # Load test data
        test_data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test.json')
        with open(test_data_path, 'r') as JSON:  # {
            self.data = json.load(JSON)
        # }
    # }

    def test_all_adj_matrix(self):
        for adj_m in self.data:   # {
            graph = Graph(adj_m.get('costs'), adj_m.get('nodes'))
            for node1 in adj_m.get('nodes'):  # {
                for node2 in adj_m.get('nodes'):  # {
                    graph.get_all_paths(node1, node2)
            # }
        # }

    def test_4x4_matrix(self):
        graph = Graph(self.data[0].get('costs'), self.data[0].get('nodes'))
        paths = graph.get_all_paths("Castle Black", "Winterfell")
        cost = 0
        for path in paths:
            cost += sum(graph.graph_dict[i][j] for i, j in zip(path, path[1::]))

        self.assertEqual(cost, 15)

    def test_4x4_matrix2(self):
        graph = Graph(self.data[0].get('costs'), self.data[0].get('nodes'))
        paths = graph.get_all_paths("Castle Black", "Riverrun")
        cost = 0
        for path in paths:
            cost += sum(graph.graph_dict[i][j] for i, j in zip(path, path[1::]))

        self.assertEqual(cost, 135)   # 55 + 80

    # TODO negative tests


if __name__ == '__main__':
    unittest.main()
