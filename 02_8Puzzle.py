
import heapq

# Goal state
GOAL = (
    "1", "2", "3",
    "4", "5", "6",
    "7", "8", "_"
)


# --------------------------------------------------
# Manhattan Distance
# --------------------------------------------------
def manhattan_distance(state):
    distance = 0

    for i in range(9):

        tile = state[i]

        # Ignore blank
        if tile == "_":
            continue

        # Current position
        current_row = i // 3
        current_col = i % 3

        # Goal position
        goal_index = GOAL.index(tile)
        goal_row = goal_index // 3
        goal_col = goal_index % 3

        distance += abs(current_row - goal_row)
        distance += abs(current_col - goal_col)

    return distance


# --------------------------------------------------
# Generate Successor States
# --------------------------------------------------
def get_successors(state):

    successors = []

    # Find blank position
    blank = state.index("_")

    row = blank // 3
    col = blank % 3

    # UP
    if row > 0:
        new_state = list(state)

        new_state[blank], new_state[blank - 3] = (
            new_state[blank - 3],
            new_state[blank]
        )

        successors.append(("UP", tuple(new_state)))

    # DOWN
    if row < 2:
        new_state = list(state)

        new_state[blank], new_state[blank + 3] = (
            new_state[blank + 3],
            new_state[blank]
        )

        successors.append(("DOWN", tuple(new_state)))

    # LEFT
    if col > 0:
        new_state = list(state)

        new_state[blank], new_state[blank - 1] = (
            new_state[blank - 1],
            new_state[blank]
        )

        successors.append(("LEFT", tuple(new_state)))

    # RIGHT
    if col < 2:
        new_state = list(state)

        new_state[blank], new_state[blank + 1] = (
            new_state[blank + 1],
            new_state[blank]
        )

        successors.append(("RIGHT", tuple(new_state)))

    return successors


# --------------------------------------------------
# Print Board
# --------------------------------------------------
def print_board(state):

    for i in range(0, 9, 3):
        print(" ".join(state[i:i + 3]))


# --------------------------------------------------
# A* Search
# --------------------------------------------------
def a_star(start):

    # Priority queue
    # Each element:
    # (f(n), g(n), state)

    frontier = []

    g = 0
    h = manhattan_distance(start)
    f = g + h

    heapq.heappush(
        frontier,
        (f, g, start)
    )

    # Explored set
    explored = set()

    # Parent of each state
    parent = {}

    # Action used to reach each state
    action_taken = {}

    # Best cost found for each state
    cost_so_far = {
        start: 0
    }

    while frontier:

        f, g, state = heapq.heappop(frontier)

        # Goal test
        if state == GOAL:

            # Reconstruct solution path
            path = []

            current = state

            while current != start:

                action = action_taken[current]

                path.append(
                    (action, current)
                )

                current = parent[current]

            # Reverse because we reconstructed
            # from goal to start
            path.reverse()

            return path

        # Ignore already explored states
        if state in explored:
            continue

        explored.add(state)

        # Generate successor states
        for action, child in get_successors(state):

            new_g = g + 1

            # If child is new OR cheaper path is found
            if (
                child not in cost_so_far
                or new_g < cost_so_far[child]
            ):

                cost_so_far[child] = new_g

                h = manhattan_distance(child)
                f = new_g + h

                parent[child] = state
                action_taken[child] = action

                heapq.heappush(
                    frontier,
                    (f, new_g, child)
                )

    # No solution
    return None


# --------------------------------------------------
# Main Program
# --------------------------------------------------
def main():

    # Read initial puzzle
    state = []

    for _ in range(3):
        state.extend(input().split())

    start = tuple(state)

    # If already at goal
    if start == GOAL:
        print("Goal State Reached")
        print("Solution Cost = 0")
        return

    # Run A*
    solution = a_star(start)

    # No solution
    if solution is None:
        print("No solution exists")
        return

    # Solution cost
    cost = len(solution)

    # --------------------------------------------------
    # Print complete solution path
    # --------------------------------------------------

    if cost == 1:
        print(f"Move: {solution[0][0]}")
        print_board(solution[0][1])

    else:
        for i, (action, state) in enumerate(solution, start=1):

            print(f"Move {i}: {action}")
            print_board(state)

    print("Goal State Reached")
    print(f"Solution Cost = {cost}")


# Run program
if __name__ == "__main__":
    main()

