import copy
"""http://www.pythontutor.com/live.html#code=import%20copy%0A%0Adef%20dict_list%28l%29%3A%0A%20%20%20%20d1%20%3D%20%7B%22k1%22%3A%20%22v1%22,%20%22k2%22%3A%20%22v2%22,%20%22k3%22%3A%20%22v3%22%20%7D%0A%20%20%20%20d2%20%3D%20%7B%22k1%22%3A%20%22v1%22,%20%22k2%22%3A%20%22v2%22,%20%22k3%22%3A%20%22v3%22%20%7D%0A%20%20%20%20d3%20%3D%20%7B%22k1%22%3A%20%22v1%22,%20%22k2%22%3A%20%22v2%22,%20%22k3%22%3A%20%22v3%22%20%7D%0A%20%20%20%20l.append%28d1%29%0A%20%20%20%20l.append%28d2%29%0A%20%20%20%20l.append%28d3%29%0A%0A%0Al1%20%3D%20%5B%5D%0Adict_list%28l1%29%0A%0A%23%20shallow%20copy%3A%20only%20copy%20the%20pointers%20of%20l1%20which%20is%20the%20pointers%20to%20the%20memory%20address%0Al2%20%3D%20l1%5B%3A%5D%0Al1%5B0%5D%5B%22k1%22%5D%20%3D%20%22changed%22%0A%0A%23%20deep%20copy%0Al3%20%3D%20copy.deepcopy%28l1%29%0Al1%5B0%5D%5B%22k1%22%5D%20%3D%20%22changed%20twice%22%0Aprint%28l3%29&cumulative=true&curInstr=17&heapPrimitives=nevernest&mode=display&origin=opt-live.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
"""


def dict_list(l):
    d1 = {"k1": "v1", "k2": "v2", "k3": "v3" }
    d2 = {"k1": "v1", "k2": "v2", "k3": "v3" }
    d3 = {"k1": "v1", "k2": "v2", "k3": "v3" }
    l.append(d1)
    l.append(d2)
    l.append(d3)


l1 = []
dict_list(l1)

# shallow copy: only copy the pointers of l1 which is the pointers to the memory address
l2 = l1[:]
l1[0]["k1"] = "changed"

# deep copy
l3 = copy.deepcopy(l1)
l1[0]["k1"] = "changed twice"
print(l3)