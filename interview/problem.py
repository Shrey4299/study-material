from collections import defaultdict


l = [8,5,3,1,6,8,3,2,7,9,1,8]

# output is [1,3,8]

repeated = []

freq = defaultdict(int)

for x in l:
    if freq[x] == 1:
        repeated.append(x)
    freq[x] += 1


print(repeated)


