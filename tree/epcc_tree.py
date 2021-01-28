#!/usr/bin/env python3

from treelib import Node, Tree
import uuid

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


# catalog_tree = Tree()
# catalog_tree.create_node("hierarchy_1", "20f39fd0-f68c-4b3a-84e8-ba5fe88270d4", data=Properties(5))
# catalog_tree.create_node("node_1_1", "23010361-d01a-4a93-959a-3779d0fe5398", parent="20f39fd0-f68c-4b3a-84e8-ba5fe88270d4", data=Properties(5))
# catalog_tree.create_node("node_1_2", "b43f1fe1-b345-4045-a5dd-cde531dec420", parent="20f39fd0-f68c-4b3a-84e8-ba5fe88270d4", data=Properties(5))

# catalog_tree.show()
# catalog_tree.show(data_property="products")

# print(catalog_tree.all_nodes())
# print(catalog_tree.level("20f39fd0-f68c-4b3a-84e8-ba5fe88270d4"))
# print(catalog_tree.depth())
# print(len(catalog_tree.children("20f39fd0-f68c-4b3a-84e8-ba5fe88270d4")))

# print(catalog_tree.get_node("23010361-d01a-4a93-959a-3779d0fe5398").data.get_products())
# print(catalog_tree.get_node("23010361-d01a-4a93-959a-3779d0fe5398").data.update_products(1))
# print(catalog_tree.get_node("23010361-d01a-4a93-959a-3779d0fe5398").data.get_products())


catalog_tree_1 = Tree()
# catalog_tree_1.create_node("hierarchy", 0)

depth = 3
width = 2

# for level in range(depth):
#     for breath in range(width):
#         catalog_tree_1.create_node("node", "node_" + str(level) + "_" + str(breath), parent="root")
#     catalog_tree_1.create_node("node", "node_" + str(level) + "_" + str(breath), parent="root")


# catalog_tree_1.show()

# parent = 0
# for idx in range(depth):
#     catalog_tree_1.create_node("node_" + str(idx + 1), idx + 1, parent=idx)

    # for node in catalog_tree_1.all_nodes():
    #     n = 1
    #     while n < width:
    #         catalog_tree_1.create_node("node_" + str(idx + 1)+str(n), str(idx + 1)+str(n), parent=idx)
    #         n = n + 1

# for node in catalog_tree_1.all_nodes():
#     if not node.is_root():
#         for idx in range(width):
#             catalog_tree_1.create_node("node_"+str(node.identifier)+str(idx), str(node.identifier)+str(idx), parent=node.identifier)

# catalog_tree_1.show()


# catalog_tree_1.show()
# for node in catalog_tree_1.all_nodes():
#     print(node.tag, node.identifier)

    # for idx in range(width**d):

# create width ^ depth of nodes
# d=1
# w=2

# p=0
# for d in (range(depth)):

    

#         for w in range(width):
#             catalog_tree_1.create_node("node_" + str(d + 1) + str(w + 1), str(d + 1) + str(w + 1), parent=p)
#         # p=str(d+1)


parent_nid = 0
parent_nodes = []

# inital root
# for idx in range(width):
#     n = Node(tag="node", identifier=uuid.uuid4())
#     parent_nodes.append(n)

# for node in parent_nodes:
#     catalog_tree_1.add_node(node, parent_nid)


for d in range(depth):

    if d == 0:
        # for idx in range(width):
        #     n = Node(tag="node", identifier=uuid.uuid4())
        #     parent_nodes.append(n)

        # for node in parent_nodes:
        #     catalog_tree_1.add_node(node, parent_nid)
        catalog_tree_1.create_node("hierarchy", 0)
        parent_nodes.append(catalog_tree_1.get_node(0))


    else:
        children_nodes = []
        # for w in range(1, width):

        for idx in range(width**d):
            n = Node(tag="node", identifier=uuid.uuid4())
            children_nodes.append(n)
        nodes = children_nodes.copy()

        for p in parent_nodes:
            for i in range(width):
                child_node = children_nodes.pop()
                catalog_tree_1.add_node(child_node, p.identifier)

        parent_nodes = nodes





# while True:
#     parent = nodes

#     for i in range(depth):
#         for j in range(width):
        
#             for i in range(width**depth):
#                 n = Node(tag="node", identifier=i + 1)
#                 nodes.append(n)



# for idx in range(width**depth):
#     n = Node(tag="node", identifier=idx + 1)
#     nodes.append(n)

# for node in nodes:
#     catalog_tree_1.add_node(node, parent_nid)












catalog_tree_1.show()
print("tag", "identifier")
print("---", "---")
for node in catalog_tree_1.all_nodes():
    print(node.tag, node.identifier)
print("------")

# print(nodes)