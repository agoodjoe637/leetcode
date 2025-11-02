from typing import List


class Solution:
    def countUnguarded(
        self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]
    ) -> int:
        grid = [[0 for x in range(n)] for y in range(m)]  # x= width, y = height

        unguardedCells = m * n - len(walls) - len(guards)

        for a, b in walls:
            grid[a][b] = "W"

        for x, y in guards:
            grid[x][y] = "G"

        for i in range(m):
            isGuarded = False
            for j in range(n):
                if grid[i][j] == "G" or grid[i][j] == "W":
                    isGuarded = False

                    if grid[i][j] == "G":
                        isGuarded = True
                elif isGuarded and grid[i][j] == 0:
                    grid[i][j] = 1
                    unguardedCells -= 1

        for i in range(m):
            isGuarded = False
            for j in range(n - 1, -1, -1):
                if grid[i][j] == "G" or grid[i][j] == "W":
                    isGuarded = False

                    if grid[i][j] == "G":
                        isGuarded = True
                elif isGuarded and grid[i][j] == 0:
                    grid[i][j] = 1
                    unguardedCells -= 1

        for j in range(n):
            isGuarded = False
            for i in range(m):
                if grid[i][j] == "G" or grid[i][j] == "W":
                    isGuarded = False

                    if grid[i][j] == "G":
                        isGuarded = True
                elif isGuarded and grid[i][j] == 0:
                    grid[i][j] = 1
                    unguardedCells -= 1

        for j in range(n):
            isGuarded = False
            for i in range(m - 1, -1, -1):
                if grid[i][j] == "G" or grid[i][j] == "W":
                    isGuarded = False
                    if grid[i][j] == "G":
                        isGuarded = True
                elif isGuarded and grid[i][j] == 0:
                    grid[i][j] = 1
                    unguardedCells -= 1

        return unguardedCells
