def count_paths_with_obstacles(m, n, obstacles):
    # Create a 2D array to store the number of paths to each point
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize the starting point
    dp[0][0] = 1

    # Mark obstacles
    for obstacle in obstacles:
        if obstacle[0] <= m and obstacle[1] <= n:
            dp[obstacle[0]][obstacle[1]] = -1

    # Update the number of paths for each point
    for i in range(m + 1):
        for j in range(n + 1):
            if dp[i][j] != -1:
                if i > 0 and dp[i - 1][j] != -1:
                    dp[i][j] += dp[i - 1][j]
                if j > 0 and dp[i][j - 1] != -1:
                    dp[i][j] += dp[i][j - 1]

    # Return the number of paths to the bottom-right corner
    return dp[m][n]

# Define the grid size
m, n = 18, 19  # Adjusted grid size to cover all obstacle points

# Define the obstacles
obstacles = [(1, 3), (3, 3), (3, 6), (4, 3), (6, 4), (6, 6), (14, 12)]

# Check the given statements
statements = [
    (1, 1, 2),
    (2, 3, 7),
    (5, 5, 51),
    (6, 7, 115),
    (8, 7, 736),
    (7, 8, 551),
    (13, 12, 883023),
    (15, 16, 37963602),
    (17, 18, 592095012)
]

for statement in statements:
    x, y, expected_paths = statement
    actual_paths = count_paths_with_obstacles(x, y, obstacles)
    is_true = actual_paths == expected_paths
    print(f"There are {actual_paths} paths to ({x},{y}): {is_true}")
