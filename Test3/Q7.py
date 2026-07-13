'''7. Online Game Leaderboard
An online gaming platform stores players' scores.
Write a program to arrange the scores in descending order so that the
leaderboard can be displayed.'''

'''Approach:
# - On a leaderboard, the HIGHEST score should be shown first (Rank 1).
# - So we need the scores sorted in descending order (biggest first).
# - We use Bubble Sort again, but flip the comparison:
#     1. Compare neighbouring scores.
#     2. Swap if the left one is SMALLER than the right one
#        (opposite of ascending sort).
#     3. Repeat until the whole list is arranged from highest to lowest.
# - Then we simply print the scores in order along with a rank number.
#
# Time Complexity: O(n^2)

# Highest score should come first, so we sort in
# descending order using Bubble Sort.'''

scores = [820, 950, 430, 999, 675, 500]

n = len(scores)

for i in range(n - 1):
    for j in range(n - 1 - i):
        if scores[j] < scores[j + 1]:      # note: < instead of > for descending
            temp = scores[j]
            scores[j] = scores[j + 1]
            scores[j + 1] = temp

print("Leaderboard (Highest to Lowest):")
rank = 1
for score in scores:
    print("Rank", rank, "-", score, "points")
    rank = rank + 1