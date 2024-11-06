# Function to calculate the maximum value in knapsack
def fractional_knapsack(capacity, values, weights):
    # Calculate value/weight ratio for each item
    ratios = [(values[i] / weights[i], values[i], weights[i]) for i in range(len(values))]
    
    # Sort items by value/weight ratio in descending order
    ratios.sort(reverse=True, key=lambda x: x[0])

    total_value = 0.0  # Total value in the knapsack
    for ratio, value, weight in ratios:
        if capacity == 0:
            break  # If the knapsack is full, stop adding items

        if weight <= capacity:
            # Take the whole item
            capacity -= weight
            total_value += value
        else:
            # Take the fraction of the item that fits
            total_value += value * (capacity / weight)
            capacity = 0  # Knapsack is now full

    return total_value

# Example usage
values = [60, 10, 120]  # Values of the items
weights = [10, 20, 30]  # Weights of the items
knapsack_capacity = 50  # Capacity of knapsack
max_value = fractional_knapsack(knapsack_capacity, values, weights)
print(f"Maximum value in Knapsack = {max_value}")