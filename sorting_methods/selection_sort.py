
lst = [4,3,8,1,9,2]

for i in range(len(lst)-1):

    for j in range(i+1, len(lst)):
        if lst[i] > lst[j]:
            lst[j], lst[i] = lst[i], lst[j]

print(lst)
