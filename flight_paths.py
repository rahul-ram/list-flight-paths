import os
import json
import sys
import click


class Graph:  # {
    """
    class to represent costs adjacent matrix in graph
    """
    def __init__(self, costs=None, nodes=None):  # {
        """
        :param costs: adjacency matrix(list of lists) representing costs
        :param nodes: names to represent nodes
        """
        self.graph_dict = {}
        self.data = {}
        if costs is None and nodes is None:  # {
            data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data.json')
            with open(data_path, 'r') as JSON:  # {
                self.data = json.load(JSON)
            # }
            self.costs = self.data.get('costs')
            self.nodes = self.data.get('nodes')
        # }
        else:  # {
            self.costs = costs
            self.nodes = nodes
        # }
        self.__check_adj_matrix()

        # create graph dictionary from costs adjacency matrix and destinations
        for idx, start in enumerate(self.nodes):  # {
            for jdx, end in enumerate(self.nodes):  # {
                if self.costs[idx][jdx] != 0:  # {
                    if self.graph_dict.get(start):  # {
                        self.graph_dict[start][end] = self.costs[idx][jdx]
                    # }
                    else:  # {
                        self.graph_dict[start] = {end: self.costs[idx][jdx]}
                    # }
                # }
            # }
        # }
    # }

    def __check_adj_matrix(self):  # {
        if not all(len(row) == len(self.costs) for row in self.costs):  # {
            sys.exit("Invalid input for costs matrix!")
        # }
        elif len(self.nodes) != len(self.costs):  # {
            sys.exit("Number of nodes does not match with Adjacency matrix dimensions!")
        # }
    # }

    def find_all_paths(self, start, end, path=[]):  # {
        """
        :param start: name of the starting node/city
        :param end: name of the destination node/city
        :param path: intermediate path
        :return: list of possible paths
        """
        path = path + [start]
        if start == end:  # {
            return [path]
        # }
        if start not in self.graph_dict:  # {
            return []
        # }
        paths = []
        for node in self.graph_dict[start]:  # {
            if node not in path:  # {
                new_paths = self.find_all_paths(node, end, path)
                for p in new_paths:  # {
                    paths.append(p)
                # }
            # }
        # }
        return paths
    # }

    def get_all_paths(self, start, end):  # {
        if start not in self.nodes:  # {
            # sys.exit(os.EX_IOERR)
            sys.exit(f"Invalid start node -> {start}")
        # }
        elif end not in self.nodes:  # {
            # sys.exit(os.EX_IOERR)
            sys.exit(f"Invalid end node -> {end}")
        # }

        paths = self.find_all_paths(start, end)
        result = ""
        for path in paths:  # {
            cost = sum(self.graph_dict[i][j] for i, j in zip(path, path[1::]))
            result += " -> ".join(str(x) for x in path) + f": {cost}\n"
        # }
        print(result)
        return paths
    # }
# }


@click.command()
@click.option('--verbose', '-v', is_flag=True, help="This will print verbose messages.")
@click.argument('source_name')
@click.argument('dest_name')
def cli(source_name, dest_name, verbose):  # {
    """cli interface entry point"""
    if not isinstance(source_name, str) or not isinstance(dest_name, str):  # {
        sys.exit(f"Arguments must be strings")
    # }
    graph = Graph()
    graph.get_all_paths(source_name, dest_name)
# }
