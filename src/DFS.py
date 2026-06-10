def checkPath(node, favOnPath=None, results=None):
    if node is None:
        return results if results is not None else {}
    
    if favOnPath is None:
        favOnPath = []
    if results is None:
        results = {}

    if node.isFavouriteFriend:
        results[node.name] = favOnPath.copy()
        favOnPath = favOnPath + [node.name]

    for child in node.children:
        checkPath(child, favOnPath, results)
    
    return results