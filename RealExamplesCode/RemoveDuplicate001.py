# Check for duplicates in list:

list1 = ['a','b','c','b','d','m','n','n']
dup_list=[]

for item in list1:
  if (list1.count(item) > 1) and (item not in dup_list):
      dup_list.append(item)

print(dup_list)

# Max Even in List
def highest_even(li):
  evn = []
  for item in li:
    if item % 2 == 0:
      evn.append(item)
  return max(evn)

print(highest_even([10,2,3,4,8,11]))