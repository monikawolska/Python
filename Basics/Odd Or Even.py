'''
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.

'''

a = input("Input number ")
number = int(a)

if number % 4 == 0:
    print("Number is multiple of 4")
elif number % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")