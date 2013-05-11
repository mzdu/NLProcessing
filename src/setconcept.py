str1 = "hello kitty, this is a funny story"

str2 = "Maklajd"

set1 = set(str1)
set2 = set(str2)

set3 = set1 & set2
set4 = set1 | set2
set5 = set1 - set2

print set3
print set4
print set5

print '-------------------------'

print set1.intersection(set2)

# you may try it, set has a lot of functions....