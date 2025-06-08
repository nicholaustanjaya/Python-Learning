scores = [88, 55, 99, 42, 70, 70, 55]

# 1. Sort the scores in ascending order
# 2. Remove duplicates
# 3. Search if 70 exists in the list
# 4. If yes, print its index (just the first one)

#1
sort_scores=sorted(scores)
print(sort_scores)
#2
remove_and_sorted_duplicate=sorted(set(scores))
print(remove_and_sorted_duplicate)
#3
print(70 in scores)
#4
print(scores.index(70))