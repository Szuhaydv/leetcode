def find_lowest_node(costs, processed):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

def print_path(parents):
    current = "fin"
    path = []
    while current is not None:
        path.append(current)
        current = parents.get(current)

    print("<-".join(path))
def dijkstra():
    graph = { "start": {"a": 6, "b": 2}, "a": {"fin": 1}, "b": {"a": 3, "fin": 5}, "fin": {} }

    costs = { "a": 6, "b": 2, "fin": float("inf") }

    parents = { "a": "start", "b": "start", "fin": None }

    processed = []

    node = find_lowest_node(costs, processed)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if new_cost < costs[n]:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_node(costs, processed)
    print_path(parents)

dijkstra()
