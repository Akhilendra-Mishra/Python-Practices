name = "Akhil"
age = 23

print("hyy my name is {}. my age is {}.". format(name ,age))

print("hyy my name is {name}. my age is {age}.")

print(f"hyy my name is {name}. my age is {age}.")

dict1 = {'age': 35, 'name': 'abc', 'salary': 45000}

val = dict1['age']

if val in dict1:
    print('This is a member of the dictionary')
else:
    print('This is not a member of the dictionary')

    bbt = {'Sheldon': 1, 'Leonard': 2}
    bbt.update({'Penny': 2})
    print(bbt)