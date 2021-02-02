#!/usr/bin/env python3

import time
import uuid

from graphviz import render
from treelib import Node, Tree

"""Build a balanced EPCC product tree consists of hierachies, nodes and products.

   docs gotes here...
"""


DEPTH = 2
WIDTH = 2


class Properties():
    def __init__(self, products: int):
        self.products = products

    def get_products(self):
        return self.products

    def update_products(self, new: int):
        self.products = new


def hierarchy(id):
    """Build a product hierachy tree."""
    hierarchy = Tree()
    parent_nodes = []

    start = time.perf_counter()
    for d in range(DEPTH + 1):
        if d == 0:
            hierarchy.create_node(id, id + "_root")
            parent_nodes.append(hierarchy.get_node(id + "_root"))

        else:
            children_nodes = []

            for idx in range(WIDTH**d):
                n = Node(tag="node", identifier=uuid.uuid4())
                children_nodes.append(n)
            nodes = children_nodes.copy()

            for p in parent_nodes:
                for i in range(WIDTH):
                    child_node = children_nodes.pop()
                    hierarchy.add_node(child_node, p.identifier)

            parent_nodes = nodes
    finish = time.perf_counter()
    print(f" Total finished in {str(round(finish-start, 2))} seconds")

    return hierarchy


def show(tree):
    tree.show(idhidden=False)
    print("tag", "identifier")
    print("---", "---")
    # for node in tree.all_nodes():
    #     print(node.tag, node.identifier)
    print("------")
    # print(f"total nodes: {len(tree.all_nodes())}")
    print(f"total nodes: {tree.size()}")

    print(','.join([str(tree[node].identifier) for node in tree.expand_tree(mode=Tree.WIDTH)]))


def draw(tree):
    tree.to_graphviz("tree.dot")
    render('dot', 'png', 'tree.dot')


h1 = hierarchy("hierarchy_1")
h2 = hierarchy("hierarchy_2")

show(h1)
show(h2)
    
print("------")

catalog = Tree()
# catalog should be store uuid
catalog.create_node("catalog", "catalog_root")
catalog.paste("catalog_root", h1)
catalog.paste("catalog_root", h2)
show(catalog)

draw(catalog)