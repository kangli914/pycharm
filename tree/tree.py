#!/usr/bin/env python3

import uuid

from graphviz import render
from treelib import Node, Tree

DEPTH = 2
WIDTH = 10


class Properties():
    def __init__(self, products: int):
        self.products = products

    def get_products(self):
        return self.products

    def update_products(self, new: int):
        self.products = new


catalog_tree = Tree()
parent_nodes = []

for d in range(DEPTH + 1):
    if d == 0:
        catalog_tree.create_node("hierarchy", "root")
        parent_nodes.append(catalog_tree.get_node("root"))

    else:
        children_nodes = []

        for idx in range(WIDTH**d):
            n = Node(tag="node", identifier=uuid.uuid4())
            children_nodes.append(n)
        nodes = children_nodes.copy()

        for p in parent_nodes:
            for i in range(WIDTH):
                child_node = children_nodes.pop()
                catalog_tree.add_node(child_node, p.identifier)

        parent_nodes = nodes


catalog_tree.show()
print("tag", "identifier")
print("---", "---")
# for node in catalog_tree.all_nodes():
#     print(node.tag, node.identifier)
print("------")
print(f"total nodes: {len(catalog_tree.all_nodes())}")

catalog_tree.to_graphviz("tree.dot")
render('dot', 'png', 'tree.dot')
