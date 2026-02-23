from collections import deque
import time


class ThreeWheelRobot:
    def __init__(self, name):
        self.name = name
        self.current_position = None

    def proximity_sensor(self):
        print("Proximity sensor scanning...")

    def gyroscope(self):
        print("Gyroscope stabilizing robot...")

    def camera(self):
        print("RGB camera capturing image...")

    def move_to(self, state):
        print(f"{self.name} moving to {state}...")
        
      
        self.proximity_sensor()
        self.gyroscope()
        self.camera()

        time.sleep(1)
        self.current_position = state
        print(f"Arrived at {state}\n")


class BFSNavigator:
    def __init__(self, graph):
        self.graph = graph

    def bfs(self, start, goal):
        visited = set()
        queue = deque([(start, [start])])

        while queue:
            node, path = queue.popleft()

            if node == goal:
                return path

            if node not in visited:
                visited.add(node)

                for neighbor in self.graph.get(node, []):
                    queue.append((neighbor, path + [neighbor]))

        return None



graph = {
    "Addis Ababa": ["Adama", "Ambo"],
    "Adama": ["Batu", "Assella"],
    "Batu": ["Shashemene"],
    "Shashemene": ["Hawassa"],
    "Hawassa": ["Dilla"],
    "Dilla": [],
    "Ambo": ["Nekemte"],
    "Nekemte": ["Gimbi"],
    "Gimbi": [],
    "Assella": []
}


robot = ThreeWheelRobot("CoffeeBot")
navigator = BFSNavigator(graph)

start_state = "Addis Ababa"
goal_state = "Dilla"

print("Searching for path...\n")

path = navigator.bfs(start_state, goal_state)

if path:
    print("Path Found:", " -> ".join(path), "\n")
    robot.current_position = start_state

    for state in path[1:]:
        robot.move_to(state)

    print("Goal Reached Successfully!")
else:
    print("No Path Found.")