import heapq



ethiopia_graph = {

    "Addis Ababa": [("Adama", 3), ("Ambo", 5), ("Debre Birhan", 5)],
    "Adama": [("Addis Ababa", 3), ("Batu", 4), ("Matahara", 3)],
    "Ambo": [("Addis Ababa", 5), ("Nekemte", 9)],
    "Debre Birhan": [("Addis Ababa", 5), ("Debre Sina", 2)],
    "Debre Sina": [("Debre Birhan", 2), ("Kemise", 6)],
    "Kemise": [("Debre Sina", 6), ("Dessie", 4)],
    "Dessie": [("Kemise", 4), ("Woldia", 6)],
    "Woldia": [("Dessie", 6), ("Lalibela", 7), ("Samara", 8)],
    "Lalibela": [("Woldia", 7), ("Sekota", 6), ("Debre Tabor", 8)],
    "Samara": [("Woldia", 8), ("Gabi Rasu", 9)],
    "Gabi Rasu": [("Samara", 9)],
    "Nekemte": [("Ambo", 9), ("Gimbi", 4)],
    "Gimbi": [("Nekemte", 4), ("Dembi Dollo", 6)],
    "Dembi Dollo": [("Gimbi", 6)],
    "Batu": [("Adama", 4), ("Shashemene", 3)],
    "Shashemene": [("Batu", 3), ("Hawassa", 1)],
    "Hawassa": [("Shashemene", 1), ("Dilla", 3)],
    "Dilla": [("Hawassa", 3), ("Bule Hora", 4)],
    "Bule Hora": [("Dilla", 4), ("Yabello", 3)],
    "Yabello": [("Bule Hora", 3), ("Moyale", 6)],
    "Moyale": [("Yabello", 6)],
    "Jimma": [("Wolkite", 8)],
    "Wolkite": [("Jimma", 8), ("Worabe", 5)],
    "Worabe": [("Wolkite", 5), ("Hossana", 2)],
    "Hossana": [("Worabe", 2), ("Wolaita Sodo", 4)],
    "Wolaita Sodo": [("Hossana", 4), ("Arba Minch", 6)],
    "Arba Minch": [("Wolaita Sodo", 6)],
    "Bale": [("Sof Oumer", 23)],
    "Sof Oumer": [("Bale", 23)],
    "Babile": [("Harar", 2)],
    "Harar": [("Babile", 2)],
    "Gondar":[("Azezo", 1),("Metema", 7),("Debarke", 4),("Humera", 9)],
    "Axum":[("Adwa", 1),("Asmera", 5),("Shire", 22)],
    "Kartum":[("Humera", 21),("Metema", 19)],
    "Asmera":[("Axum", 5),("Adigrat", 6)],
    "Adigrat":[("Asmera", 6),("Adawa", 4), ("Mekelle", 4)],
    "Adwa":[("Adigrat", 4),("Axum", 1), ("Mekelle", 7)],
    "Mekelle":[("Adigrat", 4),("Adawa", 7), ("Sekota", 9), ("Alamata", 5)],
}



def uniform_cost_search(graph, start, goal):

    priority_queue = []
    heapq.heappush(priority_queue, (0, start, [start]))

    visited = {}

    while priority_queue:

        cost, current, path = heapq.heappop(priority_queue)

        if current == goal:
            return path, cost

        if current not in visited or cost < visited[current]:
            visited[current] = cost

            for neighbor, edge_cost in graph.get(current, []):
                heapq.heappush(
                    priority_queue,
                    (cost + edge_cost, neighbor, path + [neighbor])
                )

    return None, float("inf")



def multi_goal_ucs(graph, start, goals):

    current_start = start
    total_cost = 0
    full_path = []
    individual_paths_with_costs = [] # Store individual paths and their costs

    remaining_goals = set(goals)

    while remaining_goals:

        best_goal = None
        best_path = None
        best_cost = float("inf")

        for goal in remaining_goals:
            path, cost = uniform_cost_search(graph, current_start, goal)

            if path and cost < best_cost:
                best_cost = cost
                best_goal = goal
                best_path = path

        if best_goal is None: # No path found to any remaining goal
            break

        individual_paths_with_costs.append((best_path, best_cost))
        full_path.extend(best_path[:-1])
        total_cost += best_cost
        current_start = best_goal
        remaining_goals.remove(best_goal)

    full_path.append(current_start)

    return full_path, total_cost, individual_paths_with_costs


if __name__ == "__main__":

    print("\nUCS: Addis Ababa to Lalibela")
    path, cost = uniform_cost_search(ethiopia_graph, "Addis Ababa", "Lalibela")
    print("Path:", path)
    print("Total Cost:", cost)

    print("\nMulti-Goal UCS")

    goal_states = [
      "Lalibela", "Hawassa"
    ]

    full_path, total_tour_cost, individual_paths_with_costs = multi_goal_ucs(
        ethiopia_graph,
        "Addis Ababa",
        goal_states
    )

   # print("Visit Order Path:", full_path)
    print("Total Tour Cost:", total_tour_cost)
    print("\nIndividual Paths with Costs:")
    for i, (path_segment, segment_cost) in enumerate(individual_paths_with_costs):
        print(f"  Path {i+1}: {path_segment}, Cost: {segment_cost}")