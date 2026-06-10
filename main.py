import sys
import os
from src.drawGraph import drawTree
from src.DFS import checkPath
from src.loader import loadTree

def get_file_path_gui():
    """File selection dialog (tkinter) – also works in .exe without a console."""
    try:
        from tkinter import Tk, filedialog
        Tk().withdraw()
        return filedialog.askopenfilename(title="Select data file", filetypes=[("Text files", "*.txt")])
    except Exception:
        return None

def wait_for_exit():
    """Waits for Enter key press only if stdin is available."""
    try:
        if sys.stdin.isatty():
            input("\nPress Enter to exit...")
        else:
            os.system('pause')
    except Exception:
        pass

def main():
    try:
        path = None
        if len(sys.argv) >= 2:
            path = sys.argv[1]
        else:
            path = get_file_path_gui()
            if not path:
                print("No file selected. Run the program with an argument: main.py <path>")
                wait_for_exit()
                sys.exit(1)

        root = loadTree(path)

        results = checkPath(root)
        results = checkPath(root)
        if not results:
            print("\n=== No favourite friends in the tree ===")
        else:
             print("\n=== PATH CHECK RESULTS ===\n")
             for fav, others in results.items():
                if others:
                    print(f"[CONFLICT] {fav} – other favourites on the path: {', '.join(others)}")
                else:
                    print(f"[OK] {fav} – no other favourites on the path")


        print("\n=== PATH CHECK RESULTS ===\n")
        for fav, others in results.items():
            if others:
                print(f"[CONFLICT] {fav} – other favourites on the path: {', '.join(others)}")
            else:
                print(f"[OK] {fav} – no other favourites on the path")

        print("\nPress Enter to view the graphical visualization...")
        wait_for_exit()

        drawTree(root, results)

    except Exception as e:
        print(f"\n!!! ERROR: {e}\n")
        import traceback
        traceback.print_exc()
        wait_for_exit()
        sys.exit(1)

if __name__ == "__main__":
    main()