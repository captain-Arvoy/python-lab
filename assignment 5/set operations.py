# 5.wap to enter two sets and perform all the set operations on it
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union
print("Union:", set1 | set2)

# Intersection
print("Intersection:", set1 & set2)

# Difference
print("Difference (set1 - set2):", set1 - set2)
print("Difference (set2 - set1):", set2 - set1)

# Symmetric
print("Symmetric Difference:", set1 ^ set2)

# Subset and Superset check
print("Is set1 a subset of set2?", set1 <= set2)
print("Is set1 a superset of set2?", set1 >= set2)

# Disjoint sets check
print("Are set1 and set2 disjoint?", set1.isdisjoint(set2))
