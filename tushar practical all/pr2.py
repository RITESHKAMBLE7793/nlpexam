# Function to calculate minimum edit distance
def edit_distance(a, b):
    m, n = len(a), len(b)
    dp = [[0]*(n+1) for _ in range(m+1)]

    for i in range(m+1):
        dp[i][0] = i
    for j in range(n+1):
        dp[0][j] = j

    for i in range(1, m+1):
        for j in range(1, n+1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

    return dp[m][n]


# Simple dictionary
words = ["hello", "world", "python", "spelling"]

# Input word
word = "speling"

# Find closest word
best = words[0]
min_dist = edit_distance(word, best)

for w in words:
    d = edit_distance(word, w)
    if d < min_dist:
        min_dist = d
        best = w

print("Input word:", word)
print("Correct word:", best)