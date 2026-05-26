import sys
from src.drawGraph import drawTree
from src.DFS import checkPath
from src.loader import loadTree


def main():
    if len(sys.argv) >= 2:
        path = sys.argv[1]
    else:
        path = input("Enter path to file: ").strip()

    
    try:
        root = loadTree(path)
    except FileNotFoundError:
        print(f"Error: file '{path}' not found.")
        input("Press Enter to exit...")
        sys.exit(1)

    checkPath(root)
    print()

    drawTree(root)

if __name__ == "__main__":
    main()