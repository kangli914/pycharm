#!/usr/bin/env python3

from treelib import Node, Tree

'''
- create a balance tree with x depth and y wide
- track number of products each node has
'''


class Properties():
    def __init__(self, products: int):
        self.products = products

    def get_products(self):
        return self.products

    def update_products(self, new: int):
        self.products = new


catalog_tree = Tree()
catalog_tree.create_node("hierarchy_1", "20f39fd0-f68c-4b3a-84e8-ba5fe88270d4", data=Properties(5))
catalog_tree.create_node("node_1_1", "23010361-d01a-4a93-959a-3779d0fe5398", parent="20f39fd0-f68c-4b3a-84e8-ba5fe88270d4", data=Properties(5))
catalog_tree.create_node("node_1_2", "b43f1fe1-b345-4045-a5dd-cde531dec420", parent="20f39fd0-f68c-4b3a-84e8-ba5fe88270d4", data=Properties(5))

catalog_tree.show()
catalog_tree.show(data_property="products")

print(catalog_tree.level("20f39fd0-f68c-4b3a-84e8-ba5fe88270d4"))
print(catalog_tree.depth())
print(len(catalog_tree.children("20f39fd0-f68c-4b3a-84e8-ba5fe88270d4")))

print(catalog_tree.get_node("23010361-d01a-4a93-959a-3779d0fe5398").data.get_products())
print(catalog_tree.get_node("23010361-d01a-4a93-959a-3779d0fe5398").data.update_products(1))
print(catalog_tree.get_node("23010361-d01a-4a93-959a-3779d0fe5398").data.get_products())
