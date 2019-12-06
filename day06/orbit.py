from typing import Dict

def compute_checksum(orbit, node, depth=0):
    """Return sum of direct and indirect orbits."""
    if not node in orbit:
        return depth

    checksum = depth

    for neighbor in orbit[node]:
        checksum += compute_checksum(orbit, neighbor, depth + 1)

    return checksum




def parse_input(orbit: str) -> Dict:
    """Return an adjacency list representation of the orbit map."""
    edges = [line.strip().split(')') for line in orbit.split('\n')]
    graph = {}

    for source, target in edges:
        if not graph.get(source):
            graph[source] = []

        graph[source].append(target)

    return graph

