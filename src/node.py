class Node:
    def __init__(self,name,isFavouriteFriend):
        self.name = name
        self.isFavouriteFriend = isFavouriteFriend
        self.children = []

    def addChildNode(self,child):
        self.children.append(child)

