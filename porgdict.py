student = {'name': 'John', 'age' : 25, 'courses' :  ['Math' , 'compsci']}

# print(student['courses'])
# or get method
# can  update values via following method
student['phone'] = '69420'

student['name'] = 'jane'
# get method, returns value from key or not found, instead of keyerror
print(student.get('phone', 'not found'))

#to update multiple keyvalues at the same time
student.update({'name' :'porg', 'age' : 69, 'sex' : 'yespls'})
del student['sex']

#pop method will remove but also return a value

age = student.pop('age')

# for number of keys, len
print(len(student))
# can also use print(student.values()) to see values
# to see key values pairs, print(student.items())

# to loop through keys and values:
#for key, value in student.items():
#    print(key,value)

print(student)