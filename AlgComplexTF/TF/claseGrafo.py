class Graph:
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def set_initial_weights(self):
        self.nodes[0].peso = 0