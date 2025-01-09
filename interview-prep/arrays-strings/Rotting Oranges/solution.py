class Solution:
    def orangesRotting(self, grid) -> int:
        stack = []
        num_oranges = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    stack.append((i, j))
                    num_oranges += 1
                if grid[i][j] == 1:
                    num_oranges += 1
        # we all all the rotten oranges at 0 min in the stack
        if num_oranges == 0:
            return 0
        if len(stack) == 0:
            return -1
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        time = 0
        rotten = len(stack)
        while len(stack) != 0:
            for _ in range(len(stack)):
                coordinates = stack.pop(0)
                for x, y in directions:
                    if coordinates[0]+x > -1 and coordinates[0]+x < len(grid) and coordinates[1]+y > -1 and coordinates[1]+y < len(grid[coordinates[0]+x]):
                        # valid
                        if grid[coordinates[0]+x][coordinates[1]+y] == 1:
                            grid[coordinates[0]+x][coordinates[1]+y] = 2
                            stack.append((coordinates[0]+x, coordinates[1]+y))
            rotten += len(stack)
            time += 1
        print(rotten, num_oranges, time)
        if rotten != num_oranges:
            return -1
        return time - 1
