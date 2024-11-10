import tkinter as tk
from dijkstra import dijkstra
from utils import create_graph

def run_demo():
    vertices = ['A', 'B', 'C', 'D']
    edges = {
        'A': {'B': 1, 'C': 4},
        'B': {'C': 2, 'D': 5},
        'C': {'D': 1},
        'D': {}
    }
    graph = create_graph(vertices, edges)
    try:
        path, distance = dijkstra(graph, 'A', 'D')
        message = f"Path: {' -> '.join(path)}\nTotal distance: {distance}"
    except ValueError as ve:
        message = str(ve)
    except Exception:
        message = "An unexpected error occurred."

    root = tk.Tk()
    root.title("Dijkstra Demo")
    tk.Label(root, text=message).pack(pady=20)
    tk.Button(root, text="Exit", command=root.destroy).pack(pady=10)
    root.mainloop()

if __name__ == "__main__":
    run_demo() 