courses = ['porg', 'porg2', 'porg3']
courses2 = ['porg420', 'porg69']


#adds things to start of list
courses.insert(0, 'porgfarms')
# courses.insert(0, courses2)

#append adds the list on, doesnt unpack it 
# courses.append(courses2)

#extend unpacks the list before adding it on
courses.extend(courses2)
courses.remove('porgfarms')

#removes last of list + returns it
courses.pop()


print(courses)

# sorts numbers numerically + words alphabetically. Can be reversed
courses.sort()

#

print(courses)

nums = [1, 3, 5, 7, 3, 2]
print(sorted(nums))


#To find index:
print(courses.index('porg'))

# to check if the value is in the list
print('porg' in courses)

# enumerate returns index and value. if we want to start at index 1 give 'start = 1' as 2nd arg
for index, course in enumerate(courses):
    print(index, course)
    
# to join all values in list together,
courses_str = ', '.join(courses)
print(courses_str)

# to separate all values in list
new_list = courses_str.split(' , ')

# TUPLES
# immutable, cannot add new items. 
# tuple = ('porg', 'farms') 

# Sets
# random order, no duplicate items. 
# set = {'porg', 'farms'}
# set2 = {'porg2', 'farms2'}
# intersection method = see commonality.
# Difference method = see difference
# print(set.intersection.(set2))
# print(set.difference.(set2))
# union = combine both sets
