print("Hello World")

character_name = "John"
character_age = "90"
is_male = True
print("There once was a man named " + character_name + ", ")
print("he was " + character_age + " years old.")
character_name = "Tom"
print("He really liked the name " + character_name + ", ")
print("but didn't like being " + character_age + ".")

phrase = "Giraffe Academy"
print(phrase[0] + phrase[1] + phrase[2] + phrase[3] + phrase[4] + phrase[5] + phrase[6])
print(phrase.replace("Giraffe", "Elephant"))

my_num = -5
print(abs(my_num))
print(pow(4, 2))
print(max(4, 6, 9, 23, 2, 23, 1))
print(min(4, 6, 9, 23, 2, 23, 1))
print(round(5.5))

name = input("Insert your name: ")
print("Hello" + name + "!")

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = num1 + num2
print(result)

color = input("Enter a color: ")
plural_noun = input("Enter a plural noun: ")
person = input("person: ")
print("Roses are " + color)
print(plural_noun + " are blue")
print("I love " + person)

friends = ["Anamika", "Sophie", "Katie", "Krisha", "Medha"]
friends[1] = "Anamika"
print(friends[1:4])

lucky_numbers = [2, 5, 6, 19, 30, 17, 203]
friends = ["Anamika", "Sophie", "Katie", "Krisha", "Medha"]
friends.insert(1, "NewFriend")
print(friends.index("Krisha"))
print(friends.count("Katie"))
friends.sort()
print(friends)

coordinates = (4, 5)
print(coordinates[0])


def say_hi(name, age):
    print("Hello " + name + ", you are " + age)


say_hi("Mike", "35")
say_hi("Steve", "70")


def cube(num):
    return num * num * num


result = cube(4)
print(result)

is_female = True
is_tall = True
if is_female and is_tall:
    print ("You are a tall female!")
elif is_female and not (is_tall):
    print("You are a short female!")
elif not (is_female) and is_tall:
    print("You are tall but not a female")
else:
    print("You are not female and not tall")


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(5, 9, 4))

num1 = float(input("Enter first number: "))
operator = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "/":
    print(num1 / num2)
elif operator == "*":
    print(num1 * num2)
else:
    print("Invalid operator")

month_conversions = {"Jan": "January", "Feb": "Febuary", "Mar": "March", "Apr": "April",
                     "May": "May", "Jun": "June", "Jul": "July", "Aug": "August", "Sep": "September", "Oct": "October",
                     "Nov": "November", "Dec": "December"}
print(month_conversions.get("Dec", "Not a valid Key"))

i = 1
while i <= 10:
    print(i)
    i = i + 1
print("Done with loop")

secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 5
out_of_guesses = False
while guess != secret_word and not (out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter a guess: ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("Out of guesses, You LOSE!")
else:
    print("You got it! Yay!")

friends = ["Anamika", "Sophie", "Katie"]
for index in range(len(friends)):
    print(friends[index])


def raise_to_power(base_num, pow_num):
    result = 1
    pow_negative = False
    if pow_num < 0:
        pow_negative = True
        pow_num = pow_num * -1
    for index in range(pow_num):
        result = result * base_num
    if pow_negative == True:
        result = 1.0 / result
    return result


print(raise_to_power(16, -5))

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]]
for row in number_grid:
    for col in row:
        print(col)


def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation


print(translate(input("Enter a phrase: ")))

try:
    10 / 0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError:
    print("Division by zero")
except:
    print("Invalid input")

# The following is not code to be used, please do not attempt
# It is for understanding how to read files purposes
employee_file = open("employees.txt", "r")
employee_file.close()
print(employee_file.read())

# The following code uses the file called random_file_for_python_tutorial.py
import random_file_for_python_tutorial

print(random_file_for_python_tutorial.friends)


class Student:
    def __init__(self, name, major, gpa, is_younger_than_18):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_younger_than_18 = is_younger_than_18


student1 = Student("Emma", "Finance", 3.89, True)
student2 = Student("James", "Art", "3.7", False)
print(student1.major)


class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


question_prompts = [
    "What color is the inside of watermellons?\n(a) Red\n(b) Green\n(c) Orange\n\n",
    "What color are bananas?\n(a) Teal,\n(b) Magenta\n(c) Yellow\n\n",
    "What color are grapes?\n(a) Green/Purple\n(b) Yellow\n(c) Pink\n\n"
]
questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "a")
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score = score + 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")


run_test(questions)


class Student:
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa


student1 = Student("Oscar", "Finance", 3.7)
student2 = Student("Amber", "Art", 3.9)


def on_honor_roll(self):
    if self.gpa >= 3.8:
        return True
    else:
        return False


print(student1.on_honor_roll())


class Chef:
    def make_chicken(self):
        print("The chef makes chicken")

    def make_dosa(self):
        print("The chef makes dosa")

    def make_noodles(self):
        print("The chef makes noodles")


myChef = Chef()
myChef.make_chicken()

print("Yay! I finished!!!")
