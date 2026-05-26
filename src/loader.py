from src.node import Node

def loadTree(pathToFile):
    root = None
    nodes = {}

    with open(pathToFile,'r') as f:
        for line in f:
            
            line = line.strip()

            if not line or line.startswith('#'):
                continue

            name, isFavourite, parent = line.split(',')
            isFavourite = isFavourite.strip() == "1"
            parent = parent.strip()
            
            node = Node(name,isFavourite)
            nodes[name] = node

            if parent == "None":
                root = node
            else:
                nodes[parent].addChildNode(node)
            
    return root