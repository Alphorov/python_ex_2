# Write a program that checks if a number is positive, negative, or zero.

def check_number(number: int) -> str:
    if number > 0:
        return 'The number is positive'
    elif number < 0:
        return 'The number is negative'
    else:
        return 'The number is zero'
    

# Use a for loop to print numbers from 1 to 10.
def print_numbers() -> None:
    for i in range(10):
        print(i+1)

# Use a while loop to print numbers from 10 down to 1.
def print_numbers_backwards() -> None:
    for i in range(10, 0, -1):
        print(i)

# Write a program that prints all even numbers from 1 to 20 using range().
def print_even():
    for i in range(1, 21):
        if (i % 2 == 0):
            print(i)

# Ask the user for a number. If it’s greater than 100, print "Big number!", otherwise print "Small number!".
def is_big_number():
    question: str = input("Type your number: ")

    if int(question) > 100:
        print('Big number!')
    else:
        print('Small number!')




def main():
    print(check_number(1))
    print(check_number(-1))
    print(check_number(0))

    print_numbers()
    print_numbers_backwards()

    print_even()

    is_big_number()

main()

