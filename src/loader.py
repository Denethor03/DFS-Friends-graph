from src.node import Node

def loadTree(pathToFile):
    root = None
    nodes = {}

    with open(pathToFile, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue

            parts = line.split(',')
            if len(parts) != 3:
                continue  
            name, isFavourite, parent = parts
            isFavourite = isFavourite.strip() == "1"
            parent = parent.strip()
            
            node = Node(name, isFavourite)
            nodes[name] = node

            if parent == "None":
                if root is not None:
                    raise ValueError("Multiple roots in file")
                root = node
            else:
                if parent not in nodes:
                    raise ValueError(f"Parent '{parent}' for node '{name}' has not been loaded yet")
                nodes[parent].addChildNode(node)
    
    if root is None:
        raise ValueError("No root node (parent=None) found in file")
    return root