'''4. Rank Participants
A sports academy has recorded the timings (in seconds) of participants in
a race.
Write a program to arrange the timings from the fastest to the slowest so
that the winners can be announced.'''

# Q4. Rank Participants (fastest to slowest)
# Fastest = lowest time, so we sort the timings in
# ascending order using Bubble Sort.

timings = [15.2, 12.8, 14.5, 11.9, 13.6, 16.1]

n = len(timings)

for i in range(n - 1):
    for j in range(n - 1 - i):
        if timings[j] > timings[j + 1]:
            temp = timings[j]
            timings[j] = timings[j + 1]
            timings[j + 1] = temp

print("Race Ranking (Fastest to Slowest):")
rank = 1
for time in timings:
    print("Rank", rank, "-", time, "seconds")
    rank = rank + 1