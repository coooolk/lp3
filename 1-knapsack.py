def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # Fill the DP table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]
    
    # Backtrack to find the items that were included
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        # Check if this item was included by comparing current and previous row values
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i)  # Add item index to the list
            w -= weights[i - 1]  # Reduce remaining capacity
    
    # The bottom-right corner of the table contains the maximum value
    max_value = dp[n][capacity]
    return max_value, selected_items

# Example usage
weights = [2, 3, 4, 5]
values = [1, 2, 5, 6]
capacity = 8

max_value, selected_items = knapsack(weights, values, capacity)
print("Maximum value that can be obtained:", max_value)
print("Items included:", selected_items)
