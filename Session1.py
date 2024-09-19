def hello_world():
    print("Hello World")

hello_world()


def todays_mood():
    mood = "😎"
    print("Today's mood: " + mood)

todays_mood()


# Question 3

def print_menu(menu):
    print("Lunch today is: " + menu)

print_menu('cheese')

#Question 4
a = 13
b = 27

add = (a + b)

def sum(a, b):
    return a+b


def double():
    dub = add  *2
    print(dub)

sum(a,b)
print(add)

double()


#Question 5
def product(a,b):
    prod = a * b
    print(prod)


product(22,7)

"""animalName = input()
print("name is " + animalName)
"""

#Questin 6
def classify_age():
    
    print("How old are you")
    age = int(input())

    if(age < 18):
        print("Child")
    else:
        print("Adult")

classify_age()
