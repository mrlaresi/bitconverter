#!/usr/bin/python3

# Converts input decimal number to binary format
def bina_to_deci():
    print("\nDecimal to binary converting.")
    while True:
        answer = input("Enter a number to convert >")
        if answer == "":
             break
        try:
            number = int(answer)
            print(format(number, '08b'))
        except Exception as e:
            print("Argument must be an integer.\n")
            #print(e)


# Converts input binary number to decimal format
def deci_to_bina():
    print("\nBinary to decimal converting.")
    while True:
        answer = input("Enter a binary to convert >")
        if answer == "":
            break
        try:
            if (is_binary(answer)):
                print(int(answer, 2))
            else: 
                raise Exception("")
        except Exception as e:
            print("Input must be in binary format.\n")
            #print(e)


def to_hexa():
    print("\nConverting to hexadecimal.")
    while True:
        answer = input("Enter binary/decimal to convert >")
        if answer == "":
            break
        try:
            if (is_binary(answer)):
                print(hex(int(answer, 2)))
            else:
                print(hex(int(answer)))
        except Exception as e:
            print("Input is neither decimal or binary.\n")
            #print(e)


def hex_to_deci():
    print("\nHexadecimal to decimal converting.")
    while True:
        answer = input("Enter hexadecimal number to convert >").lower()
        if answer == "":
            break
        try:
            print(int(answer, 16))
        except Exception as e:
            print("Input must be a hexadecimal number.")
            #print(e)

def hex_to_char():
    print("\nHexadecimal to UTF8 character.")
    while True:
        answer = input("Enter hexadecimal number to convert >").lower()
        if answer == "":
            break
        try:
            print(bytes.fromhex(answer).decode("UTF8"))
        except Exception as e:
            print("Input must be a hexadecimal number.")
            #print(e)

def is_binary(st):
    for char in st:
        if (char != "1" and char != "0"):
            return False
    return True

# Gets the switchcase from the dictionary
def switch_case(argument):
    switch = switcher.get(argument, "")
    switch()


# Dictionary holding the different switchcases
switcher = {
        1: bina_to_deci,
        2: deci_to_bina,
        3: hex_to_deci,
        4: hex_to_char,
        5: to_hexa
    } 

def main():
    print("Welcome. Enter an empty string to exit at any moment.\n")
    while True:
        choises = len(switcher)
        print("Choose what to convert.")
        print("  1: for decimal to binary")
        print("  2: for binary to decimal")
        print("  3: for hexadecimal to decimal")
        print("  4: for hexadecimal to UTF8")
        print("  5: for binary/decimal to hexa")
        try:
            answer = input("> ")
            if answer == '':
                break
            answer = int(answer)
            if 0 < answer and answer <= choises:
                switch_case(answer)
            else:
                raise Exception('')
        except Exception as e:
            print("\nMust be an integer between 1-{}.".format(choises))
            #print(e)
    print("\nGoodbye.")

if __name__ == "__main__":
    main()
