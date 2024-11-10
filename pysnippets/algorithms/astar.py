import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0  # Cost from start to current node
        self.h = 0  # Heuristic cost from current node to end
        self.f = 0  # Total cost (g + h)

    def __eq__(self, other):
        return self.position == other.position

    def __lt__(self, other):
        return self.f < other.f

def astar(maze, start, end, allow_diagonal=False):
    start_node = Node(start)
    end_node = Node(end)

    open_list = []
    closed_list = set()
    open_dict = {}  # Dictionary to track nodes and their 'g' values

    heapq.heappush(open_list, start_node)
    open_dict[start_node.position] = start_node

    while open_list:
        current_node = heapq.heappop(open_list)
        closed_list.add(current_node.position)

        if current_node == end_node:
            # Reconstruct path
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # Return path in correct order

        children = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
        if allow_diagonal:
            # Include diagonal movements (top-left, top-right, bottom-left, bottom-right)
            directions += [(-1, -1), (-1, 1), (1, -1), (1, 1)]

        # Generate children (neighbors)
        for new_position in directions:
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Skip out-of-bounds or blocked cells (value != 0 means wall)
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[0]) - 1) or node_position[1] < 0:
                continue
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            new_node = Node(node_position, current_node)
            children.append(new_node)

        for child in children:
            if child.position in closed_list:
                continue  # Ignore already evaluated nodes

            child.g = current_node.g + 1  # g value is distance from start
            # Using Manhattan distance as heuristic (for non-diagonal movement)
            child.h = abs(child.position[0] - end_node.position[0]) + abs(child.position[1] - end_node.position[1])
            child.f = child.g + child.h

            # Check if this node should be added to open_list or skipped
            if child.position not in open_dict or child.g < open_dict[child.position].g:
                open_dict[child.position] = child
                heapq.heappush(open_list, child)

    return None  # Return None if no path is found

# Example usage:
maze = [
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0]
]

start = (0, 0)
end = (4, 5)

# Calling the A* algorithm with diagonal movement allowed
path = astar(maze, start, end, allow_diagonal=True)
print("Path:", path)