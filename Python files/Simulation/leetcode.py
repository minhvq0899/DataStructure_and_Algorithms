"""
Name: Minh Q. Vu

This python file is a part of my effort in getting myself refreshed with Data Structure and Algorithms concepts so
I can later tackle Leetcode challenges with more confidence. 

========================================================= Simulation =========================================================

Class Leetcode

    (Hard)
    Leetcode 428. Serialize and Deserialize N-ary Tree (Premium + Hard)

"""

from typing import List


class Robot:
    def __init__(self, room, start_row, start_col):
        self.room = room              # 2D grid: 1=open, 0=blocked
        self.x = start_row            # Current row position
        self.y = start_col            # Current column position
        self.d = 0                    # Facing direction (0=up, 1=right, 2=down, 3=left)
        self.cleaned = set()         # Set of cleaned positions

        self.directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Up, Right, Down, Left

    def move(self):
        """Try to move forward. Return True if successful, else False."""
        dx, dy = self.directions[self.d]
        nx, ny = self.x + dx, self.y + dy
        if 0 <= nx < len(self.room) and 0 <= ny < len(self.room[0]) and self.room[nx][ny] == 1:
            self.x, self.y = nx, ny
            return True
        return False

    def turnLeft(self):
        """Turn 90 degrees left."""
        self.d = (self.d - 1) % 4

    def turnRight(self):
        """Turn 90 degrees right."""
        self.d = (self.d + 1) % 4

    def clean(self):
        """Clean the current cell."""
        self.cleaned.add((self.x, self.y))


class Solution:
    def cleanRoom(self, robot):
        # Directions: Right, Down, Left, Up (clockwise)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        visited = set()

        # Backtrack: move back and restore orientation
        def goBack():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        def dfs(x, y, d):
            """
            DFS traversal from position (x, y) facing direction d.
            The robot explores clockwise, always turning right.
            """
            visited.add((x, y))
            robot.clean()

            for k in range(4):
                new_d = (d + k) % 4
                dx, dy = directions[new_d]
                nx, ny = x + dx, y + dy

                if (nx, ny) not in visited and robot.move():
                    dfs(nx, ny, new_d)

                goBack()

                # Always turn robot right before next direction
                robot.turnRight()

        # Start DFS from (0, 0), facing right (direction 0)
        dfs(0, 0, 0)
        



if __name__ == "__main__":
    # Example room layout
    room = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]

    # Start at (1, 0) — left-middle of the grid
    robot = Robot(room, 1, 0)

    # Use your existing DFS cleaner
    Solution().cleanRoom(robot)

    # Print cleaned cells
    print("Cleaned cells:", sorted(robot.cleaned))




