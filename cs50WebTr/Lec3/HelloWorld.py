import datetime
print("Hello, World!")

company = ["Pixar", "Apple", "Next"]
company.sort()

name = "Steve"
age = datetime.datetime.now().year - 1990
print(f"Steve - my name is {name} and i daied {age} years ago")

myName = input("Steve - What about you? What is your name ? ")
print(f"{myName} - My name is {myName}")

myAge = int(input(f"Steve - How old are you, {myName}? "))
if myAge < 0:
    print("Steve - You are not born yet!")
elif myAge == 0:
    print("Steve - You are a newborn!")
elif myAge < 18:
    print("Steve - You are a minor!")
elif myAge < 65:
    print("Steve - You are an adult!")
else:
    print("Steve - You are a senior citizen!")
    
print(f"Steve - I know how to spell your name {myName}!")
for char in myName:
    print(f"Steve - {char}")
    
print("Steve - Nice to meet you!")
print("Steve - Here are some companies I Worked for:")
for comp in company:
    print(f"Steve - {comp}")


def greet(person):
    print(f"Steve - Hello, {person}!")
    
def dead(year_born):
    current_year = datetime.datetime.now().year
    return current_year - year_born