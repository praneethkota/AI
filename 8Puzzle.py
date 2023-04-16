from collections import deque
# Define the initial and goal states of the puzzle
initial_state = [[2, 8, 3],[1, 6, 4],[7, 0, 5]]
goal_state = [[1, 2, 3],[8, 0, 4],[7, 6, 5]]
def bfs(initial_state, goal_state):
    # Create a queue containing only the initial state
    queue = deque([initial_state])
    # Create a dictionary containing the parent state of each state
    parent = {tuple(map(tuple, initial_state)): None}
    # Loop until the queue is empty
    while queue:
        # Dequeue the next state from the front of the queue
        state = queue.popleft()
        # Check if the current state is the goal state
        if state == goal_state:
            # Reconstruct the path from the initial state to the goal state
            path = []
            while state is not None:
                path.append(state)
                state = parent[tuple(map(tuple, state))]
            return list(reversed(path))
        # Find the position of the empty tile (represented by 0)
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    break
            if state[i][j] == 0:
                break
        # Generate all possible moves from the current state
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            new_i, new_j = i + di, j + dj
            if 0 <= new_i < 3 and 0 <= new_j < 3:
                # Create a new state by swapping the empty tile with the adjacent tile
                new_state = [row[:] for row in state]
                new_state[i][j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[i][j]
                # Check if the new state has already been visited
                if tuple(map(tuple, new_state)) not in parent:
                    # Enqueue the new state and mark its parent as the current state
                    queue.append(new_state)
                    parent[tuple(map(tuple, new_state))] = state
    # If the goal state is not found, return None
    return None
# Call the BFS function to solve the puzzle
path = bfs(initial_state, goal_state)
if path:
    print("Solution found:")
    for state in path:
        for row in state:
            print(row)
        print()
else:
    print("No solution found.")
