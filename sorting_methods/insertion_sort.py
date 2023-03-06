lst = [4, 3, 8, 1, 9, 2]

n = len(lst)
for i in range(1, n):

    key = lst[i]

    j = i - 1
    while j >= 0 and key < lst[j]:
        lst[j + 1] = lst[j]
        j -= 1
    lst[j + 1] = key

print(lst)
