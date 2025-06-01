#--Conditional statements

# if condition:
    # This block executes if the condition is True.
# elif another_condition:
    # coed block if another condition is true.
# else:
    # code block if all conditions are false.

age = int(input('Enter your age: '))

if age < 18:
    print('You are a child')
elif age < 30:
    print('You are younger')
else:
    print('You are an adult')

#--Loops

#--for loop example
for i in range(50):
    print('Iteration: ', i)

#--while loop example
count = 0
while count < 10:
    print('Count: ', count)
    count += 1

#--break and continue statements
for i in range(10):
    if i == 5:
        break
    if i == 0:
        continue
    print('Current Number :', i)

#--Exercise: