def get_graph_from(edges, nodes_count):
    graph = [[] for _ in range(nodes_count)]
    for source, target in edges:
        graph[source].append(target)
    return graph


def calculate_suspicious_nodes(graph, k):
    suspicious = set()

    def dfs(node):
        suspicious.add(node)
        for adj in graph[node]:
            if adj not in suspicious:
                dfs(adj)

    dfs(k)
    return suspicious


def exists_node_invoking_suspicious_node(graph, suspicious_nodes):
    visited = set()

    def dfs(node):
        if node in suspicious_nodes:
            return True
        if node in visited:
            return False
        visited.add(node)
        for adj in graph[node]:
            if dfs(adj):
                return True
        return False

    for i in range(len(graph)):
        if i not in suspicious_nodes and dfs(i):
            return True
    return False


class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph = get_graph_from(invocations, n)
        suspicious = calculate_suspicious_nodes(graph, k)
        if exists_node_invoking_suspicious_node(graph, suspicious):
            return list(range(n))
        return list(set(range(n)) - suspicious)