
def checkPath(node,favOnPath = None):

    if favOnPath is None:
        favOnPath = []

    if node.isFavouriteFriend:
        if favOnPath:
            print(f"There are other friends on the path to {node.name}: {', '.join(favOnPath)}")
        else:
            print(f"There are no other favourite friends on the path to {node.name}")
        favOnPath = favOnPath + [node.name]
    
    for child in node.children:
        checkPath(child,favOnPath)