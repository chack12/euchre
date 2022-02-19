from collections import Counter
from itertools import chain, combinations
from random import shuffle

# Init player count, pair lists, tables.
players = [1,2,3,4,5,6,7,8]
pairs   = []
table1  = []
table2  = []

# Generate combination for 8 players, each paired with eachother once.
for subset in combinations(players, 2):
    pairs.append(list(subset))


# Looped until pair count reaches zero.
while len(pairs) > 0:

    shuffle(pairs)

    pair1 = pairs.pop()
    pair2 = pairs.pop()
    pair3 = pairs.pop()
    pair4 = pairs.pop()

    total = list(Counter(chain(pair1,pair2,pair3,pair4)))

    if len(total) != len(players):
        shuffle(pairs)
        pairs.append(pair1)
        pairs.append(pair2)
        pairs.append(pair3)
        pairs.append(pair4)
    else:
        table1.append(pair1 + pair2)
        table2.append(pair3 + pair4)

print("\n")
print("Table 1      Table 2")

for table in range(len(table1)):
    print(table1[table], table2[table])