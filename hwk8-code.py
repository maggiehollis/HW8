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

def combineArrays(a1:list, a2:list) -> list:
    """ Combine two given arrays into one large array, equivalent to a1.append(a2)
    :param a1: (list) the first array
    :param a2: (list) the second array
    :return : (list) the two arrays combined into one larger array
    >>> combineArrays([1,2,3], [4,5])
    [1,2,3,4,5]
    """
    arr = new_array(len(a1) + len(a2))
    for i in range(0, len(a1)): # add the values of a1
        arr[i] = a1[i]
    for j in range(0, len(a2)): # add the values of a2
        arr[len(a1)+j] = a2[j]
    return arr
    
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
            path = combineArrays([node], path)
    return path


# Main:
graph: dict[str | None, dict[str, int] | None] = {
    "king": {"scales": 1 * 60 + 7},
    "scales": {
        "king": 1 * 60 + 7,
        "ziskind": 4 * 60 + 5,
        "campus center": 3 * 60 + 52,
        "tyler": 6 * 60 + 54,
    },
    "ziskind": {"scales": 4 * 60 + 5, "cutter": 0},
    "cutter": {
        "ziskind": 0,
        "capen": 2 * 60 + 27,
        "lamont": 0,
        "northrop": 1 * 60 + 45,
    },
    "capen": {"cutter": 2 * 60 + 27, "talbot": 50},
    "talbot": {"capen": 50, "dunkin donuts": 9 * 60 + 48, "lamont": 53},
    "lamont": {"cutter": 0, "talbot": 53, "gillett": 1 * 60 + 12, "chase": 2 * 60 + 16},
    "northrop": {"cutter": 1 * 60 + 45, "gillett": 10, "jmg": 1 * 60 + 4},
    "gillett": {"lamont": 1 * 60 + 12, "northrop": 10, "chase": 1 * 60 + 19},
    "chase": {"lamont": 2 * 60 + 16, "gillett": 1 * 60 + 19, "duckett": 37},
    "duckett": {
        "chase": 37,
        "dunkin donuts": 13 * 60 + 7,
        "neilson": 3 * 60 + 11,
        "ford": 5 * 60 + 30,
    },
    "dunkin donuts": {"talbot": 9 * 60 + 48, "duckett": 13 * 60 + 7},
    "campus center": {"scales": 3 * 60 + 52, "jmg": 53, "chapin": 47},
    "jmg": {"northrop": 1 * 60 + 4, "campus center": 53, "hatfield": 43},
    "chapin": {"campus center": 47, "wright hall": 47},
    "hatfield": {"jmg": 43, "neilson": 1 * 60 + 10, "wright hall": 1 * 60 + 16},
    "wright hall": {"chapin": 47, "neilson": 42, "hatfield": 1 * 60 + 16},
    "neilson": {
        "duckett": 3 * 60 + 11,
        "hatfield": 1 * 60 + 10,
        "wright hall": 42,
        "tyler": 0,
        "ford": 0,
    },
    "tyler": {
        "scales": 6 * 60 + 54,
        "neilson": 0,
        "sage hall": 1 * 60 + 25,
        "rugby pitch": 4 * 60 + 11,
    },
    "ford": {"duckett": 5 * 60 + 30, "neilson": 0, "sage hall": 2 * 60 + 19},
    "sage hall": {"tyler": 1 * 60 + 25, "ford": 2 * 60 + 1},
    "rugby pitch": {"tyler": 4 * 60 + 11},
}

path = run_dijkstra(graph, "king", "neilson")
print("The shortest path is", path)
