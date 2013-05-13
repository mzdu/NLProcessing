list1 = ['b','c','d','e','f','g']
list2 = ['b','c','d','e']
list3 = ['a','k']

# compare set1 with set2, set(list2) is a subset of set(list1), so say False
print set(list1) < set(list2)

# if we directly compare two lists, 
# they will only compare the sequence of their first elements
# since 'a' is less than 'b', then return True
print list3 < list1