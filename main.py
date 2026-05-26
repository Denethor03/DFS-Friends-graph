import sys
from src.drawGraph import drawTree
from src.DFS import checkPath
from src.loader import loadTree


def main():
    if len(sys.argv) < 2:
        print("Usage: main.exe <path_to_file>")
        sys.exit(1)
    
    root = loadTree(sys.argv[1])
    if root:
        checkPath(root)
        drawTree(root)

if __name__ == "__main__":
    main()