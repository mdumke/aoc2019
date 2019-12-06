from typing import Dict

def count_orbital_transfers(orbit_map, start, target) -> int:
    """Return the number of hops beween node's and target's orbit.

    Args:
        orbit_map (Dict): Adjacency list representation of an orbital map.
            Assumes the graph is unweighted and bi-directional.
        start (str): Name of the starting node.
        target (str): Name of the target node.

    Returns:
        int: The number of orbital transfers (hops) from the starting
            orbit the the target's orbit.
    """
    # build up a routing table for the orbit map
    visited = set()
    routes = {}

    fringe = []
    fringe.append((start, None))

    while fringe:
        node, parent = fringe.pop(0)

        if node in visited:
            continue

        visited.add(node)
        routes[node] = parent

        for neighbor in orbit_map[node]:
            if neighbor not in visited:
                fringe.append((neighbor, node))

    # backtrack path from target to start
    current = target
    hops = 0

    while current != start:
        current = routes[current]
        hops += 1

    return hops - 2


def compute_checksum(orbit, start) -> int:
    """Return sum of direct and indirect orbits."""
    checksum = 0

    visited = set()
    fringe = []
    fringe.append((start, None, 0))

    while fringe:
        node, parent, depth = fringe.pop(0)

        if node in visited:
            continue

        visited.add(node)
        checksum += depth

        for neighbor in orbit[node]:
            if neighbor not in visited:
                fringe.append((neighbor, node, depth + 1))

    return checksum


def parse_input(orbit_map: str) -> Dict:
    """Return an adjacency list representation of the orbit map."""
    edges = [line.strip().split(')') for line in orbit_map.split('\n')]

    # create an orbit map as an unweighted, bi-directional graph
    graph = {}

    for source, target in edges:
        if not graph.get(source):
            graph[source] = []

        if not graph.get(target):
            graph[target] = []

        graph[source].append(target)
        graph[target].append(source)

    return graph

