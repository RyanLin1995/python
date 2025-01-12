graph = {}
graph["start"] = {}
graph["start"]["a"] = 10

graph["a"] = {}
graph["a"]["b"] = 20

graph["b"] = {}
graph["b"]["fin"] = 30
graph["b"]["c"] = 1

graph["c"] = {}
graph["c"]["a"] = 1

graph["fin"] = {}

infinity = float("inf")

costs = {}
costs["a"] = 10
costs["b"] = infinity
costs["c"] = infinity
costs["fin"] = infinity

parents = {}
parents["a"] = "start"
parents["b"] = None
parents["c"] = None
parents["fin"] = None

processed = []


def find_lowest_cost_node(costs):
    lowest_cost = infinity
    lowest_cost_node = None

    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node

    return lowest_cost_node


node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]

    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

if __name__ == '__main__':
    # 回溯路径
    def reconstruct_path(parents, start, end):
        path = [end]
        while path[-1] != start:
            path.append(parents[path[-1]])
        path.reverse()
        return path


    print(reconstruct_path(parents, "start", "fin"))
