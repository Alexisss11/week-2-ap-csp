
# ----------------------------------------
# Print Practice Exercises
# ----------------------------------------

# Print Practice #1
# Write Python code that prints the sentence: I love learning Python
print("I love learning Python")


# Print Practice #2
# Write Python code that prints the sentence: Learning with 'TOTAL Python' is super fun!
print("Learning with 'TOTAL Python' is super fun!")


# Print Practice #3
# Write Python code that prints the number 555 to the screen as a result of a mathematical expression
print(500 + 55)

##############################################################################################################
# Find 3 objects around the room and create variables from it,
# Insert those variables into an f-string sentence(look at slide 22)in repl.it
object1 = "computer"
object2 = "Lizbeth"
object3 = "Alexis"
print(f"I see {object1}, {object2}, and {object3}")

# Familiarize yourself with the syntax of the print() function.
# Print your name.
name = "Kalexis"
print("Name:", name)
# Print today's date.
date = "10/30"
print("Date:", date)
# Print the name of your favorite movie.
print("The Death of a Unicorn")
# Print your name and age on separate lines using a single print() function.
print(name)
age = 16
print(age)
# Use f-strings to print a message like: "In 10 years, [Your Name] will be [Your Age + 10] years old."
print(f"In 2 years, your name will be {name} and you will be {age + 2}")
##############################################################################################################

###########################String Practice##################################
#syntax is the way we write code
# print("Hello World")
# name = "John"
#in other languages, this is different
# in javascript for example, you define
#variables with let or const or var5
#in python, you just give your variables a
#name and then define it with a value


#challenge
# find a summary of the movie blue beetle online and create a 
# variable called blue_beetle_summary and print it it out to the screen
blue_beetle_summary = "Jaime Reyes suddenly finds himself in possession of an ancient relic of alien biotechnology called the Scarab. When the Scarab chooses Jaime to be its symbiotic host, he's bestowed with an incredible suit of armor that's capable of extraordinary and unpredictable powers, forever changing his destiny as he becomes the superhero Blue Beetle."
print(f"{blue_beetle_summary}")
print("Length of blue_beetle_summary:", len(blue_beetle_summary))
# print the length of the sum"mary
# upper case the entire summary 
print("Uppercase:", blue_beetle_summary.upper())
# print the summary
# print the summary in lowercase

print("Lowercase:", blue_beetle_summary.lower())
# replace the word blue with red 
new_text = blue_beetle_summary.replace("blue", "red")
print(new_text)
# print the summary 
# string index the word beetle and print it out
print("Beetle")
# print the last word of the summary
# print the summary in reverse
reversed_string = blue_beetle_summary[::-1]
print(reversed_string)

##########################input practice#############################################
#input is when we ask the user for input/data
# Ask the user to enter their name.

# Input Practice #1
# Write Python code that allows the user to enter their answer, by making them the following question:
# What are you learning today?
# Your code must be able to print to the screen whatever is entered by the user (use the print function).
question = input("What are you learning today?:")
print(f"{question}")
# Input Practice #2
# Write Python code that allows the user to enter their answer, by making them the following question:
# Where are you from?
question2 = input("Where are you from?")
print(f"{question2}")
# Your code must be able to print to the screen whatever is entered by the user (use the print function).

# Input Practice #3
# Write Python code that displays the user's full name on the screen, by allowing them to enter their first and last name with the following instructions:
# What is your name?
question3 = input("What is your name?")
question4 = input("What is your surname")
print(f"Your name is {question3} {question4}")
# What is your surname?
# The code must be able to print the user's first and last name on the screen, separated by a space.

# Exercise:
# Write a program that asks the user for their name and favorite color, then prints a message using both pieces of information.

name_question = input("What is your name?:")
fav_color = input("What is your favorite color?:")
print(f"Hello! My name is {name_question} and my favorite color is {fav_color}")
