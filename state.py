
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
                "name": "$", # Using $ to represent the empty string
                "arrows": dict()
            }
        ]
        for i in range(len(sequence)):
            self.nodes.append(
                {
                    "name": sequence[:i + 1], # So that we skip over empty
                    "arrows": dict()
                }
            )

    def compute_connections(self):
        for index, node in enumerate(self.nodes[:-1]):
            # Don't need connections for the last node, since that's the end!
            if node["name"] == "$":
                name = ""
                # Using $ to represent the empty string
            else:
                name = node["name"]
            for outcome in self.ALPHABET:
                modified = name + outcome # What the next sequence would read
                offset = 1 # Initially want to get to next node
                finished = False
                while index + offset > 0 and not finished:
                    # Index + offset > 0 means we can still access a node
                    if modified == self.nodes[index + offset]["name"]:
                        node["arrows"][outcome] = index + offset
                        finished = True
                    else:
                        modified = modified[1:]
                        # We ignore the first letter of modified, to see
                        # If we're partway through a different match
                        offset -= 1 # Look at the previous node
                if not finished: # I.e. never found a matching node
                    node["arrows"][outcome] = 0 # Back to the start

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
