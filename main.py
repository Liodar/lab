user_name = 'Sasha'
print(user_name)

user_age = 19
print("Hi, my name is ", user_name, ", I am ", user_age, " years old.")

name5 = (user_name + '') * 5
print(name5)

# user_name = input("Hi! What's your name?")
# user_age = input("And now, what's your age?")
try:
    user_age = int(user_age)
except Exception:
    print("Age have to be in numbers. "
          "Please, enter your age correctly.")

if (user_age > 150) or (user_age < 0):
    raise Exception("Age is out of truly bounds. "
                    "Please enter correct age.")

print("Nice to meet u, " + user_name + "! Are u going well in this age? ;)")

int_user_age = int(user_age)
if int_user_age >= 18:
    print("Oh, it's nice to chat with you.")
else:
    print("Who is this little cutie?")

print(user_name[2:len(user_name) - 1])
print(user_name[::-1])
print(user_name[-3:len(user_name)])
print(user_name[:5])

print(len(user_name))
summ = 0
mltp = 0
while user_age != 0:
    summ += user_age % 10
    mltp *= user_age % 10
    user_age /= 10
print(summ, mltp)

print(user_name.lower(), user_name.upper())

try:
    test = input("What is the answer for this 2+2*2?")
    test = int(test)
    if test != 6:
        print("Sorry, the answer is wrong. :(")
    else:
        print("Yay! Correct answer! :)")
except Exception:
    print("Answer have to be wrote in numbers. "
          "Please, wrote correct form of answer.")
