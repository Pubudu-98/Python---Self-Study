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