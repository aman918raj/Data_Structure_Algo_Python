
lst = [4,3,8,1,9,2]

for i in range(len(lst)-1):
    min_idx = i
    for j in range(i+1, len(lst)):
        if lst[min_idx] > lst[j]:
            min_idx = j
    lst[min_idx], lst[i] = lst[i], lst[min_idx]

print(lst)
