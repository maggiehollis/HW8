# Name:       - Maggie, Kiera, Ashby, Ashley
# Peers:      - names of CSC252 students who you consulted or "N/A"
# References: - URL of resources used or "N/A"


#### HELPER FUNCTIONS - START ####
def new_array(length: int) -> list[str]:
    """Helper function to make a new array of a given length

    Args:
        length (int): length for the new array

    Returns:
        list[int]: new array of desired length

    >>> new_array(2)
    ["", ""]
    """
    L = [""] * length
    return L


#### HELPER FUNCTIONS - END ####


def get_initial_parents(
    graph: dict[str | None, dict[str, int] | None], initial: str
) -> dict[str, str | None] | None:
    parents: dict[str, str | None] = {}
    for node in graph.keys():
        if node != None and node != initial:
            parents[node] = None
    initial_neighbors = graph[initial]
    if initial_neighbors == None:  # Error Checking
        return None
    for key in initial_neighbors.keys():
        parents[key] = initial
    return parents


def get_initial_costs(
    graph: dict[str | None, dict[str, int] | None], initial: str
) -> dict[str, int | float] | None:
    costs: dict[str, int | float] = {}
    for node in graph.keys():
        if node != None:
            costs[node] = float("inf")
    initial_neighbors = graph[initial]
    if initial_neighbors == None:  # Error Checking
        return None
    for key, value in initial_neighbors.items():
        costs[key] = value
    return costs


def find_lowest_cost_node(
    costs: dict[str, int | float], processed: list[str]
) -> str | None:
    lowest_cost: float = float("inf")
    lowest_cost_node: str | None = None
    # Go through each node.
    for node in costs:
        cost = costs[node]
        # If it's the lowest cost so far and hasn't been processed yet...
        if cost < lowest_cost and node not in processed:
            # ... set it as the new lowest-cost node.
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def run_dijkstra(
    graph: dict[str | None, dict[str, int] | None], start: str, finish: str
) -> list[str] | list[str | None]:
    processed: list[str] = new_array(len(graph.keys()))
    i = 0
    parents = get_initial_parents(graph, start)
    if parents is None:
        return processed
    costs = get_initial_costs(graph, start)
    if costs is None:
        return processed
    node = find_lowest_cost_node(costs, processed)

    while node is not None and node not in processed:
        cost = costs[node]
        neighbors = graph[node]
        if neighbors is None:
            node = find_lowest_cost_node(costs, processed)
            continue
        for n in neighbors.keys():
            new_cost: int | float = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed[i] = node
        i += 1
        node = find_lowest_cost_node(costs, processed)

    path = [finish]
    node = finish
    while node and node != start:
        if parents.get(node) != None:
            node = parents[node]
            path = [node] + path
    return path


# Main:
graph: dict[str | None, dict[str, int] | None] = {
    "king": {"scales": 0},
    "scales": {"king": 0, "ziskind": 0, "campus center": 0, "tyler": 0},
    "ziskind": {"scales": 0, "cutter": 0},
    "cutter": {"ziskind": 0, "capen": 0, "lamont": 0, "northrop": 0},
    "capen": {"cutter": 0, "talbot": 0},
    "talbot": {"capen": 0, "dunkin donuts": 0, "lamont": 0},
    "lamont": {"cutter": 0, "talbot": 0, "gillett": 0, "chase": 0},
    "northrop": {"cutter": 0, "gillett": 0, "jmg": 0},
    "gillett": {"lamont": 0, "northrop": 0, "chase": 0},
    "chase": {"lamont": 0, "gillett": 0, "duckett": 0},
    "duckett": {"chase": 0, "dunkin donuts": 0, "neilson": 0, "ford": 0},
    "dunkin donuts": {"talbot": 0, "duckett": 0},
    "campus center": {"scales": 0, "jmg": 0, "chapin": 0},
    "jmg": {"northrop": 0, "campus center": 0, "hatfield": 0},
    "chapin": {"campus center": 0, "wright hall": 0},
    "hatfield": {"jmg": 0, "neilson": 0},
    "wright hall": {"chapin": 0, "neilson": 0},
    "neilson": {"duckett": 0, "hatfield": 0, "wright hall": 0, "tyler": 0, "ford": 0},
    "tyler": {"scales": 0, "neilson": 0, "sage hall": 0, "rugby pitch": 0},
    "ford": {"duckett": 0, "neilson": 0, "sage hall": 0},
    "sage hall": {"tyler": 0, "ford": 0},
    "rugby pitch": {"tyler": 0},
}

path = run_dijkstra(graph, "king", "neilson")
print("The shortest path is", path)


# the graph
# graph = {}
# graph["start"] = {}
# graph["start"]["a"] = 6
# graph["start"]["b"] = 2

# graph["a"] = {}
# graph["a"]["fin"] = 1

# graph["b"] = {}
# graph["b"]["a"] = 3
# graph["b"]["fin"] = 5

# graph["fin"] = {}

# the costs table
# infinity = float("inf")
# costs = {}
# costs["a"] = 6
# costs["b"] = 2
# costs["fin"] = infinity

# the parents table
# parents = {}
# parents["a"] = "start"
# parents["b"] = "start"
# parents["fin"] = None
