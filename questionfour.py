class MiniMax:
    def __init__(self, tree):
        self.tree = tree

    def minimax(self, node, maximizing_player):
        # If terminal node
        if isinstance(self.tree[node], int):
            return self.tree[node]

        if maximizing_player:
            max_eval = float('-inf')
            for child in self.tree[node]:
                eval = self.minimax(child, False)
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            for child in self.tree[node]:
                eval = self.minimax(child, True)
                min_eval = min(min_eval, eval)
            return min_eval

    def best_move(self, start):
        best_value = float('-inf')
        best_state = None

        for child in self.tree[start]:
            value = self.minimax(child, False)
            print(f"Evaluating move to {child}: Utility = {value}")

            if value > best_value:
                best_value = value
                best_state = child

        print("\nBest Move:", best_state)
        print("Best Utility Achievable:", best_value)
        return best_state, best_value


tree = {
    "Addis Ababa": ["Ambo", "Buta Jirra", "Wolkite", "Adama"],

    "Ambo": ["Nekemte"],
    "Nekemte": ["Gimbi", "Limu"],
    "Gimbi": 8,
    "Limu": 8,

    "Buta Jirra": ["Worabe"],
    "Worabe": ["Hossana", "Durame"],
    "Hossana": 6,
    "Durame": 5,

    "Wolkite": ["Bench Naji", "Tepi"],
    "Bench Naji": 5,
    "Tepi": 6,

    "Adama": ["Diredawa", "Mojo"],
    "Diredawa": ["Harar", "Chiro"],
    "Harar": 10,
    "Chiro": 6,
    "Mojo": ["Dilla", "Kaffa"],
    "Dilla": 9,
    "Kaffa": 7
}

game = MiniMax(tree)

game.best_move("Addis Ababa")