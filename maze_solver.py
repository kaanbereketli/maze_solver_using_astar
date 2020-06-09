import math
from timeit import default_timer as timer

node_counter = 0

class Square():

    def __init__(self, parent=None, location=None):
        global node_counter
        self.parent = parent
        self.location = location

        self.g = 0
        self.h = 0
        self.f = 0
        node_counter = node_counter +1

    def __eq__(self, other):
        return self.location == other.location

    def __hash__(self):
        return hash(self.location)

def astar(maze, start, end):
    """Returns a list of tuples"""

    # Create start and end square
    start_square = Square(None, start)
    #start_square.g = start_square.h = start_square.f = 0
    end_square = Square(None, end)
    #end_square.g = end_square.h = end_square.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = set()

    # Add the start square
    open_list.append(start_square)

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current square
        current_square = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_square.f:
                current_square = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.add(current_square)

        # Found the goal
        if current_square == end_square:
            path = []
            current = current_square
            while current is not None:
                path.append(current.location)
                current = current.parent
            return path[::-1] # Return reversed path

        # Generate children
        children = []
        for new_location in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares

            # Get square location
            square_location = (current_square.location[0] + new_location[0], current_square.location[1] + new_location[1])

            # Make sure within range
            if square_location[0] > (len(maze) - 1) or square_location[0] < 0 or square_location[1] > (len(maze[len(maze)-1]) -1) or square_location[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[square_location[0]][square_location[1]] != 0:
                continue

            # Create new square
            new_square = Square(current_square, square_location)

            # Append
            children.append(new_square)

        # Loop through children
        for child in children:

            # Child is on the closed list
            if child in closed_list:
                continue

            # Generate f, g, and h values
            child.g = current_square.g + 1
            child.h = math.sqrt((child.location[0] - end_square.location[0]) ** 2) + ((child.location[1] - end_square.location[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_square in open_list:
                if child == open_square and child.g > open_square.g:
                    continue

            # Add the child to the open list
            open_list.append(child)


def main():

    maze = [[0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
            [0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
            [0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
            [0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]]

    maze2 = [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
            [0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
            [0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    #Additional maze for further usage to test different sizes
    maze3 = [[0, 1, 0, 0, 0, 1],
            [0, 1, 0, 1, 0, 1],
            [0, 1, 0, 1, 0, 1],
            [0, 1, 0, 1, 0, 1],
            [0, 1, 0, 1, 0, 1],
            [0, 0, 0, 1, 0, 1],
            [0, 0, 0, 1, 0, 1]]

    maze4 = [[0, 1, 0, 0],
            [0, 1, 0, 1],
            [0, 1, 0, 1],
            [0, 0, 0, 1]]


    start = (0, 0)
    end = (0, 9)

    start_time = timer()
    path = astar(maze, start, end)
    end_time = timer()
    print("Time passed:", end_time - start_time, "seconds")
    print("Nodes traversed: " + str(node_counter))

    for i in path:
        tempx = i[0]
        tempy = i[1]
        maze[tempx][tempy] = 9

    print(path)
    print("\n")
    for row in range(len(maze)):
        print(maze[row])


if __name__ == '__main__':
    main()