# loops until 3 then break breaks loop

nums = [1, 2, 3, 4, 5]

for num in nums:
    if num == 3:
        print('found')
        break
    print(num)
    
# if it was replaced by a continue statement, it would head straight to next iteration in loop without reaching print statement.

porgs = [1, 2, 3, 4, 5]

for porg in porgs:
    for letter in 'abc':
        print(num, letter)
        
# to scroll through 1-10 (this makes it start at 1 and go up to but not including 11)
for i in range(1,11):
    print(i)
    
x = 0

while x <10:
    if x==5:
        break
    print(x)
    x+= 1 
