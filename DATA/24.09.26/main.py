def min_cost_tickets(n):
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        cost_1 = dp[i - 1] + 2
        cost_3 = dp[max(0, i - 3)] + 5
        cost_7 = dp[max(0, i - 7)] + 10
        dp[i] = min(cost_1, cost_3, cost_7)

    return dp[n]


n_days = 10
print(f"Мінімальна вартість для {n_days} днів:", min_cost_tickets(n_days))