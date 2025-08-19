# 🚑 Emergency Vehicle Routing System

This mini-project demonstrates how **graph algorithms (BFS & DFS)** can be applied to real-world problems like **emergency vehicle routing in urban cities**.
It helps simulate how ambulances, fire trucks, or police vehicles can find the **shortest path** in a road network using **Breadth-First Search (BFS)** and compare it with **Depth-First Search (DFS)**.

---

## 📌 Features

* Visualize the city road network as a graph (nodes = locations, edges = roads).
* Input **start** and **goal** locations through GUI.
* **BFS Path** → Finds & animates the shortest path.
* **DFS Path** → Finds & animates a possible path (not always shortest).
* **Best Path** → Compares BFS vs DFS paths.
* Ambulance animation showing the route step-by-step.

---

## 🛠️ Tools & Technologies

* **Language**: Python 3.x
* **Libraries**:

  * `Tkinter` → GUI development
  * `NetworkX` → Graph creation & visualization
  * `Matplotlib` → Graph plotting & animation
  * `Collections (deque)` → Efficient BFS queue
* **IDE**: VS Code / PyCharm / Jupyter Notebook
* **OS**: Windows / Linux / Mac

---

## 📂 Project Structure

```
📦 Emergency-Vehicle-Routing
 ┣ 📜 main.py              # Project source code
 ┣ 📜 README.md            # Project documentation
 ┗ 📂 screenshots          # Output screenshots
```

---

## 🏗️ System Architecture

1. **Graph Representation**

   * Nodes → Locations (Hospital, School, Mall, Fire Station, etc.)
   * Edges → Roads between locations

2. **Algorithms**

   * **BFS** → Finds shortest path in unweighted graphs
   * **DFS** → Explores a path (not always shortest)

3. **GUI Components**

   * Start & Goal input fields
   * Buttons: BFS Path | DFS Path | Best Path | Clear
   * Ambulance route animation

---

## ▶️ How to Run

1. Clone the repository

   ```bash
   git clone https://github.com/your-username/emergency-routing-system.git
   cd emergency-routing-system
   ```
2. Install dependencies

   ```bash
   pip install matplotlib networkx
   ```
3. Run the project

   ```bash
   python main.py
   ```

---

## 📸 Screenshots

*(Add your project screenshots here for better visualization)*

---

## 📚 References

* [NetworkX Documentation](https://networkx.org/documentation/stable/)
* [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
* [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)
* Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. *Introduction to Algorithms*, MIT Press.

---

## ✅ Conclusion

This project shows the practical application of **graph algorithms** in real-life emergency routing.
It highlights why **BFS is preferred** over DFS for shortest-path problems in unweighted graphs, while also providing an interactive and educational GUI simulation.

---

Do you want me to also **add a section with sample outputs (like BFS vs DFS path results)** inside the README so it’s more engaging for recruiters or GitHub visitors?
