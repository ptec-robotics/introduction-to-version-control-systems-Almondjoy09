my_list=[ 4, 456, 234, 68]

print("unsorted", my_list )

my_list.sort()

print("sorted",  my_list)

l1= [1,8,2,234,7,45]
print("original list", l1)

for i in range(0, len(l1)):
    for j in range(i+1, len(l1)):
        if l1[i] >= l1[j]:
            l1[i], l1[j] = l1[j],l1[i]
print("sorted list", l1)