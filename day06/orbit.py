from typing import List, Dict

Graph = Dict[str, List[str]]
Table = Dict[str, str]

def count_orbital_transfers(orbit_map: Graph, start: str, target: str) -> int:
    """Return the number of hops beween node's and target's orbit.

    Args:
        orbit_map (Dict): Adjacency list representation of an orbital map.
            Assumes the graph is unweighted and bi-directional.
        start (str): Name of the starting node.
        target (str): Name of the target node.

    Returns:
        int: The number of orbital transfers (hops) from the starting
            orbit to the target's orbit.
    """
    routes = build_routing_table(orbit_map, start)
    path = find_path(routes, target)

    # do not count start and target as hops
    return len(path) - 2


def find_path(routes: Table, target: str) -> List[str]:
    """Return a path to from route's start to target node."""
    path = []
    current = target

    while current:
        path.append(current)
        current = routes[current]

    # ignore the starting node itself
    return path[1:]


def build_routing_table(graph: Graph, start: str) -> Table:
    """Return a routing table for the given starting node.

    A routing table captures node-parent relationships within a graph.
    It can be used to identify paths from any given node to the
    starting node.
    """
    routes = {}

    visited = set()
    fringe = []
    fringe.append((start, None))

    while fringe:
        node, parent = fringe.pop(0)

        if node in visited:
            continue

        visited.add(node)
        routes[node] = parent

        for neighbor in graph[node]:
            if neighbor not in visited:
                fringe.append((neighbor, node))

    return routes


def compute_checksum(orbit_map: Graph, start: str) -> int:
    """Return sum of direct and indirect orbits."""
    routes = build_routing_table(orbit_map, start)
    checksum = 0

    for node in orbit_map.keys():
        path = find_path(routes, node)
        checksum += len(path)

    return checksum


def parse_input(orbit_map: str) -> Graph:
    """Return an adjacency list representation of the orbit map."""
    edges = [line.strip().split(')') for line in orbit_map.split('\n')]

    # create an orbit map as an unweighted, undirected graph
    graph = {}

    for source, target in edges:
        graph[source] = graph.get(source) or []
        graph[source].append(target)

        graph[target] = graph.get(target) or []
        graph[target].append(source)

    return graph

