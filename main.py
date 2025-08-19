import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import networkx as nx
from collections import deque
import time


class RoadNetwork:
    def __init__(self):
        self.graph = {}

    def add_road(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs_shortest_path(self, start, goal):
        visited = set()
        queue = deque([[start]])
        if start == goal:
            return [start]
        while queue:
            path = queue.popleft()
            node = path[-1]
            if node not in visited:
                for neighbor in self.graph.get(node, []):
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)
                    if neighbor == goal:
                        return new_path
                visited.add(node)
        return None

    def dfs_path(self, start, goal):
        stack = [[start]]
        visited = set()
        while stack:
            path = stack.pop()
            node = path[-1]
            if node == goal:
                return path
            if node not in visited:
                visited.add(node)
                for neighbor in self.graph.get(node, []):
                    new_path = list(path)
                    new_path.append(neighbor)
                    stack.append(new_path)
        return None


class EmergencyRoutingUI:
    def __init__(self, root, city):
        self.root = root
        self.city = city
        self.root.title("🚑 Emergency Vehicle Routing System")
        self.root.geometry("520x500")
        self.root.configure(bg="#f0f8ff")

        tk.Label(root, text="🚦 Emergency Routing System 🚦", font=("Arial", 14, "bold"), bg="#f0f8ff", fg="#2c3e50").pack(pady=10)
        tk.Button(root, text="🗺 Show City Map", command=self.show_graph, bg="#3498db", fg="white", font=("Arial", 10, "bold")).pack(pady=5)

        self.points_label = tk.Label(root, text="Available Points: " + ", ".join(city.graph.keys()), font=("Arial", 9), bg="#f0f8ff")
        self.points_label.pack(pady=5)

        tk.Label(root, text="Enter Start Location:", bg="#f0f8ff").pack()
        self.start_entry = tk.Entry(root)
        self.start_entry.pack(pady=5)

        tk.Label(root, text="Enter Goal Location:", bg="#f0f8ff").pack()
        self.goal_entry = tk.Entry(root)
        self.goal_entry.pack(pady=5)

        button_frame = tk.Frame(root, bg="#f0f8ff")
        button_frame.pack(pady=15)

        tk.Button(button_frame, text="🚑 BFS Path", command=self.find_bfs_path, bg="#27ae60", fg="white", font=("Arial", 10, "bold"), width=15).grid(row=0, column=0, padx=10)
        tk.Button(button_frame, text="🚑 DFS Path", command=self.find_dfs_path, bg="#e67e22", fg="white", font=("Arial", 10, "bold"), width=15).grid(row=0, column=1, padx=10)
        tk.Button(button_frame, text="⭐ Best Path", command=self.compare_paths, bg="#8e44ad", fg="white", font=("Arial", 10, "bold"), width=15).grid(row=1, column=0, columnspan=2, pady=10)
        tk.Button(button_frame, text="❌ Clear", command=self.clear_inputs, bg="#c0392b", fg="white", font=("Arial", 10, "bold"), width=15).grid(row=2, column=0, columnspan=2, pady=10)

    def clear_inputs(self):
        self.start_entry.delete(0, tk.END)
        self.goal_entry.delete(0, tk.END)

    def show_graph(self):
        G = nx.Graph()
        for u in self.city.graph:
            for v in self.city.graph[u]:
                G.add_edge(u, v)
        pos = nx.spring_layout(G, seed=42)
        plt.figure(figsize=(7, 6))
        nx.draw(G, pos, with_labels=True, node_size=1000, node_color="lightblue", font_size=9, font_weight="bold")
        plt.title("City Road Network", fontsize=14)
        plt.show()

    def find_bfs_path(self):
        start, goal = self.start_entry.get().strip(), self.goal_entry.get().strip()
        if start not in self.city.graph or goal not in self.city.graph:
            messagebox.showerror("Error", "Invalid start or goal location!")
            return
        path = self.city.bfs_shortest_path(start, goal)
        if not path:
            messagebox.showinfo("Result", f"No path found between {start} and {goal}")
            return
        self.animate_ambulance(path, "BFS Shortest Path")

    def find_dfs_path(self):
        start, goal = self.start_entry.get().strip(), self.goal_entry.get().strip()
        if start not in self.city.graph or goal not in self.city.graph:
            messagebox.showerror("Error", "Invalid start or goal location!")
            return
        path = self.city.dfs_path(start, goal)
        if not path:
            messagebox.showinfo("Result", f"No path found between {start} and {goal}")
            return
        self.animate_ambulance(path, "DFS Path Found")

    def compare_paths(self):
        start, goal = self.start_entry.get().strip(), self.goal_entry.get().strip()
        if start not in self.city.graph or goal not in self.city.graph:
            messagebox.showerror("Error", "Invalid start or goal location!")
            return

        bfs_path = self.city.bfs_shortest_path(start, goal)
        dfs_path = self.city.dfs_path(start, goal)

        if not bfs_path or not dfs_path:
            messagebox.showinfo("Result", f"No path found between {start} and {goal}")
            return

        result_text = (
            f"📌 BFS Path: {' -> '.join(bfs_path)} (length {len(bfs_path)-1})\n"
            f"📌 DFS Path: {' -> '.join(dfs_path)} (length {len(dfs_path)-1})\n\n"
            f"✅ Best Algorithm: BFS (always finds the shortest path in unweighted graphs).\n"
            f"❌ DFS may take longer and does not guarantee the shortest route."
        )
        messagebox.showinfo("Comparison Result", result_text)

    def animate_ambulance(self, path, title_text):
        G = nx.Graph()
        for u in self.city.graph:
            for v in self.city.graph[u]:
                G.add_edge(u, v)
        pos = nx.spring_layout(G, seed=42)

        plt.ion()
        fig, ax = plt.subplots(figsize=(7, 6))

        for i in range(len(path)):
            ax.clear()
            nx.draw(G, pos, with_labels=True, node_size=1000, node_color="skyblue", font_size=9, font_weight="bold")
            nx.draw_networkx_nodes(G, pos, nodelist=path[:i+1], node_color="lightgreen")
            if i > 0:
                nx.draw_networkx_edges(G, pos, edgelist=[(path[i-1], path[i])], width=3, edge_color="red")
            ax.text(pos[path[i]][0], pos[path[i]][1]+0.05, "🚑", fontsize=16, ha='center')
            plt.title(f"{title_text}: {' -> '.join(path[:i+1])}", fontsize=14)
            plt.draw()
            plt.pause(1)

        plt.ioff()
        plt.show()


if __name__ == "__main__":
    city = RoadNetwork()
    city.add_road("Hospital", "School")
    city.add_road("Hospital", "Mall")
    city.add_road("School", "Library")
    city.add_road("Mall", "Cinema")
    city.add_road("Mall", "Park")
    city.add_road("Library", "PoliceStation")
    city.add_road("Cinema", "Stadium")
    city.add_road("Park", "Temple")
    city.add_road("PoliceStation", "Stadium")
    city.add_road("Temple", "FireStation")
    city.add_road("Stadium", "FireStation")


    root = tk.Tk()
    app = EmergencyRoutingUI(root, city)
    root.mainloop()
