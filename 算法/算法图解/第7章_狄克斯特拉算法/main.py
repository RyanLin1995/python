# 实现狄克斯特拉算法

# 初始化一个空字典 graph 用于存储图结构，键是节点名称，值是相邻节点及其权重。
graph = {}
# 添加起始节点 "start" 及其相邻节点 "a" 和 "b"，权重分别为 6 和 2。
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
# 添加相邻节点 "a" 及其相邻节点 "fin"，权重分别为 1。
graph["a"] = {}
graph["a"]["fin"] = 1
# 添加相邻节点 "b" 及其相邻节点 "a" 和 "fin"，权重分别为 3 和 5。
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
# 添加终点节点 "fin"，它没有相邻节点。
graph["fin"] = {}

# 定义一个表示无穷大的变量 infinity，用于初始化未知路径的成本。
infinity = float("inf")  # 无穷大

# 定义一个字典 costs，用于存储节点的成本。
costs = {}
# 初始时，从起点到 "a" 的成本为 6，到 "b" 的成本为 2，到 "fin" 的成本为无穷大（未知）。
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# 定义一个字典 parents，用于存储每个节点的父节点。
parents = {}
# 初始时，"a" 的父节点为 "start"，"b" 的父节点为 "start"，"fin" 的父节点为 None。
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

# 定义一个列表 processed，用于记录已经处理过的节点。
processed = []


# 定义一个函数 find_lowest_cost_node，用于找到成本最小的节点。
def find_lowest_cost_node(costs):
    """
    定义函数 find_lowest_cost_node，用于找到当前未处理的、成本最低的节点：
        * 初始化 lowest_cost 为无穷大，lowest_cost_node 为 None。
        * 遍历 costs 中的所有节点，如果某个节点的成本小于当前最低成本且未被处理过，则更新最低成本和对应的节点。
        * 返回成本最低的节点。
    """
    lowest_cost = float("inf")  # 无穷大
    lowest_cost_node = None

    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


# 使用狄克斯特拉算法的核心逻辑:
node = find_lowest_cost_node(costs)  # 找到当前未处理的、成本最低的节点 node。
while node is not None:
    cost = costs[node]  # 获取当前节点的成本 cost。
    neighbors = graph[node]  # 获取当前节点的所有相邻节点 neighbors。

    for n in neighbors.keys():  # 遍历相邻节点。
        new_cost = cost + neighbors[n]  # 计算相邻节点的成本。
        if costs[n] > new_cost:  # 如果相邻节点的成本大于当前成本，则更新成本和对应的父节点。
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)  # 将当前节点标记为已处理。
    node = find_lowest_cost_node(costs)  # 找到下一个未处理的、成本最低的节点。

if __name__ == '__main__':
    print(costs)
    print(parents)
