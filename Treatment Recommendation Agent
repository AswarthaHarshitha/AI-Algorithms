class TreatmentAgent:
    def __init__(self):
        self.options = {
            "A": {"e": 0.9, "s": 0.2},
            "B": {"e": 0.7, "s": 0.1},
            "C": {"e": 0.8, "s": 0.3},
        }

    def utility(self, e, s):
        return e - s

    def recommend(self):
        best = None
        max_u = -float('inf')

        for k, v in self.options.items():
            u = self.utility(v["e"], v["s"])
            if u > max_u:
                max_u = u
                best = k

        return best

# Example
agent = TreatmentAgent()
print(agent.recommend())
