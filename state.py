
"""
Each finite state machine has a list of nodes, which look like this:

Node = {
    name: string,
    arrows: dict(str, int)
}

Each node will be indexed by a number, and have a name as well.
The "arrows" property indicates where the node will point to.
Basically, you access arrows, and then index by the outcome.
The number output is the next node to point to.

For now, it'll just be for sequences of heads and tails.
"""

class FiniteStateMachine:

    ALPHABET = "H", "T"

    def __init__(self, sequence: str):
        self.nodes = [
            {
                "name": "$",
                "arrows": dict()
            }
        ]
        for i in range(len(sequence)):
            self.nodes.append(
                {
                    "name": sequence[:i + 1],
                    "arrows": dict()
                }
            )

    def compute_connections(self):
        for index, node in enumerate(self.nodes[:-1]):
            if node["name"] == "$":
                name = ""
            else:
                name = node["name"]
            for outcome in self.ALPHABET:
                modified = name + outcome
                offset = 1
                finished = False
                while index + offset > 0 and not finished:
                    if modified == self.nodes[index + offset]["name"]:
                        node["arrows"][outcome] = index + offset
                        finished = True
                    else:
                        modified = modified[1:]
                        offset -= 1
                if not finished:
                    node["arrows"][outcome] = 0

    def __repr__(self):
        result = ""
        for node in self.nodes:
            result += node["name"] + "\n"
            for outcome, pointer in node["arrows"].items():
                result += outcome + ":" + self.nodes[pointer]["name"] + "\n"
        return result

y = FiniteStateMachine("HTTHHHTH")
y.compute_connections()
print(y)
