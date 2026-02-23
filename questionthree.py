import heapq

graph = {
    "Addis Ababa": [("Adama", 3), ("Ambo", 5), ("Debre Birhan", 5)],
    "Adama": [("Batu", 4), ("Assella", 4), ("Addis Ababa", 3)],
    "Batu": [("Shashemene", 3)],
    "Shashemene": [("Hawassa", 1)],
    "Hawassa": [("Dilla", 3)],
    "Dilla": [("Bule Hora", 4)],
    "Bule Hora": [("Yabello", 2)],
    "Yabello": [("Moyale", 6)],
    "Moyale": []
}

heuristic = {
    "Addis Ababa": 26,
    "Adama": 23,
    "Batu": 19,
    "Shashemene": 16,
    "Hawassa": 15,
    "Dilla": 12,
    "Bule Hora": 8,
    "Yabello": 6,
    "Moyale": 0,
    "Ambo": 31,
    "Debre Birhan": 31,
    "Assella": 22
}

class AStarSearch:
    def __init__(self, graph, heuristic):
        self.graph = graph
        self.heuristic = heuristic

    def search(self, start, goal):
        open_list = []
        heapq.heappush(open_list, (self.heuristic[start], 0, start, [start]))

        visited = {}

        while open_list:
            f_cost, g_cost, current, path = heapq.heappop(open_list)

            if current == goal:
                print("Goal reached!")
                print("Total Cost:", g_cost)
                print("Path:", " -> ".join(path))
                return path, g_cost

            if current in visited and visited[current] <= g_cost:
                continue

            visited[current] = g_cost

            for neighbor, cost in self.graph.get(current, []):
                new_g = g_cost + cost
                new_f = new_g + self.heuristic.get(neighbor, 0)

                heapq.heappush(open_list, (new_f, new_g, neighbor, path + [neighbor]))

        print("No path found.")
        return None, float("inf")


astar = AStarSearch(graph, heuristic)

astar.search("Addis Ababa", "Moyale")