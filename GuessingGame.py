#   2nd project


import random


#   For user to guess the num
def user_geussing():
    print("\tWelcome to Guessing Game.")
    print("\tEnter lower bound and upper bound to guess a number from.")
    lower_bound = int(input("\tlower Bound : "))
    upper_bound = int(input("\tUpper Bound : "))
    rand_number = random.randint(lower_bound, upper_bound)
    found = 0
    while found != 1:
        x = int(input("\tEnter a number : "))
        if x == rand_number:
            found = 1
        else:
            if x < rand_number:
                print("\tYour guess is too low.")
                continue
            else:
                print("\tYour guess is too high")
                continue
    print("\tCongratulations you guessed the number correctly")


#   For computer to guess the num with help of user    
def computer_guessing():
    print("\tEnter a number to be guessed by the computer.")
    desired_number = int(input("\tYour number between 1 and 100 : "))
    found = 0
    upper_bound = 100
    lower_bound = 1
    ran_num = random.randint(lower_bound, upper_bound)
    while found != 1:
        ran_num = random.randint(lower_bound, upper_bound)
        if ran_num == desired_number:
            found = 1
        else:
            print("\t", ran_num, ": is the guessed number.\n\t Enter (h) if this number is too high or Enter (l) if "
                                 "this number is too low.")
            x = input("(h/l) : ")
            if x == 'h':
                upper_bound = ran_num - 1
                continue
            else:
                lower_bound = ran_num + 1
                continue
    print("\tGuessed the number correctly : ", ran_num)


#   For computer to guesss the number without help of user    
def computer_guessing_automatic():
    print("\tEnter a number to be guessed by the computer.")
    desired_number = int(input("\tYour number between 1 and 100 : "))
    found = 0
    upper_bound = 100
    lower_bound = 1
    ran_num = random.randint(lower_bound, upper_bound)
    while found != 1:
        ran_num = random.randint(lower_bound, upper_bound)
        if ran_num == desired_number:
            found = 1
        else:
            if ran_num < desired_number:
                print(ran_num, " is too low.")
                lower_bound = ran_num + 1
                continue
            else:
                print(ran_num, " is too high.")
                upper_bound = ran_num - 1
                continue
    print("\tGuessed the number correctly : ", ran_num)


print("\tWelcome! ")
print("\tEnter (u) if you want to guess the number. \n Enter (c) if you want computer to guess your number."
      "\n\tEnter (a) if you want computer to guess your number without you giving hint.(without h/l)")
a = str(input('Enter y/n : '))
if a == 'u':
    user_geussing()
elif a == 'a':
    computer_guessing_automatic()
else:
    computer_guessing()
print("\tThank You for playing.")
