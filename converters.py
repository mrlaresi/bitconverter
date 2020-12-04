#!/usr/bin/env python

def deci_to_bina(input):
    '''Converts input decimal number to binary format'''
    try:
        return bin(int(input))
    except:
        return ""

def hex_to_bina(input):
    '''Converts input hex number to binary format'''
    try:
        return bin(int(input, 16))
    except:
        return ""

def str_to_bina(input):
    '''Converts input UTF-8 string to binary format'''
    try:
        return ''.join(map(bin, bytearray(input, "utf-8")))
    except:
        return ""



def bina_to_deci(input):
    '''Converts input binary to decimal format'''
    try:
        return str(int(input, 2))
    except:
        return ""

def hex_to_deci(input):
    '''Converts input hex number to decimal format'''
    try:
        return str(int(input, 16))
    except:
        return ""



def bina_to_hexa(input):
    '''Converts input binary to hexadecimal format'''
    try:
        return hex(int(input, 2))
    except:
        return ""

def deci_to_hexa(input):
    try:
        return hex(int(input))
    except:
        return ""


'''def hex_to_char():
    print("\nHexadecimal to UTF8 character.")
    while True:
        answer = input("Enter hexadecimal number to convert >").lower()
        if answer == "":
            break
        try:
            print(bytes.fromhex(answer).decode("UTF8"))
        except Exception as e:
            print("Input must be a hexadecimal number.")
            #print(e)'''