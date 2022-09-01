val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)


def knapSack(W, wt, val, n):
    # print("ddd")
    if W == 0 or n == 0:
        return 0
    if wt[n - 1] <= W:
        # print(val[n-1])
        return max(val[n - 1] + knapSack(W - wt[n - 1], wt, val, n - 1), knapSack(W, wt, val, n - 1))
    elif wt[n - 1] > W:
        # print(val[n-1])
        return knapSack(W, wt, val, n - 1)


print(knapSack(W, wt, val, n))


# A Dynamic Programming based Python
# Program for 0-1 Knapsack problem
# Returns the maximum value that can
# be put in a knapsack of capacity W


def knapSack_memo(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1]
                              + K[i - 1][w - wt[i - 1]],
                              K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    return K[n][W]


print(knapSack_memo(W, wt, val, n))

# This code is contributed by Bhavya Jain
