#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// Function to solve the 0/1 Knapsack problem using dynamic programming
int knapsack(int capacity, vector<pair<int, int>>& items) {
    int n = items.size();
    vector<vector<int>> dp(n + 1, vector<int>(capacity + 1, 0));

    // Build the dp table
    for (int i = 1; i <= n; i++) {
        for (int w = 1; w <= capacity; w++) {
            if (items[i - 1].second <= w) {
                // Choose the maximum between not taking or taking the item
                dp[i][w] = max(dp[i - 1][w], items[i - 1].first + dp[i - 1][w - items[i - 1].second]);
            } else {
                // If item can't be included, carry forward the value
                dp[i][w] = dp[i - 1][w];
            }
        }
    }

    return dp[n][capacity]; // Maximum profit for the given capacity
}

int main() {
    int n;
    cout << "Enter the number of items: ";
    cin >> n;

    vector<pair<int, int>> items(n); // Each pair holds (profit, weight)
    for (int i = 0; i < n; i++) {
        cout << "Enter the profit and weight of item " << i + 1 << ": ";
        cin >> items[i].first >> items[i].second;
    }

    int capacity;
    cout << "Enter the capacity of the knapsack: ";
    cin >> capacity;

    int maxProfit = knapsack(capacity, items);
    cout << "The maximum profit is: " << maxProfit << endl;

    return 0;
}
