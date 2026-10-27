
def depth_limited_search(node, goal, graph, limit, path):
    if node == goal:
        return path + [node]

    if limit == 0:
        return "cutoff"

    cutoff_occurred = False

    for child in graph.get(node, []):
        if child not in path:
            result = depth_limited_search(
                child, goal, graph, limit - 1, path + [node]
            )

            if isinstance(result, list):
                return result

            if result == "cutoff":
                cutoff_occurred = True

    if cutoff_occurred:
        return "cutoff"
    return "failure"


def iterative_deepening_search(initial, goal, graph, maximum_depth):
    for depth in range(maximum_depth + 1):
        result = depth_limited_search(
            initial, goal, graph, depth, []
        )

        if isinstance(result, list):
            return result

    return None


# Main program
print("ITERATIVE DEEPENING DEPTH-FIRST SEARCH (IDDFS)")

initial = input("Enter Initial State: ").strip()
goal = input("Enter Goal State: ").strip()
maximum_depth = int(input("Enter Maximum Depth: "))

graph = {}

print("\nEnter the search tree (one node per line).")
print("Format: A: B, C")
print("Enter END when finished.")
print("Use - for nodes with no children.\n")

while True:
    line = input().strip()

    if line.upper() == "END":
        break

    if not line:
        continue

    node, children_text = line.split(":", 1)
    node = node.strip()
    children_text = children_text.strip()

    if children_text == "-" or not children_text:
        graph[node] = []
    else:
        graph[node] = [
            child.strip()
            for child in children_text.split(",")
            if child.strip()
        ]

result = iterative_deepening_search(
    initial, goal, graph, maximum_depth
)

print("\nResult:")

if result is not None:
    print("Goal found!")
    print("Path:", " -> ".join(result))
    print("Depth:", len(result) - 1)
else:
    print("Goal not found within the maximum depth.")
