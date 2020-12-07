#!/usr/bin/env python

"""def deci_to_bina(string):
    '''Converts input decimal number to binary format'''
    try:
        return bin(int(string))
    except:
        return ""

def hex_to_bina(string):
    '''Converts input hex number to binary format'''
    try:
        return bin(int(string, 16))
    except:
        return ""

def octa_to_bina(string):
    '''Converts input octal number to binary format'''
    try:
        return bin(int(string, 8))
    except:
        return ""

def str_to_bina(string):
    '''Converts input UTF-8 string to binary format'''
    try:
        return ''.join(map(bin, bytearray(string, "utf-8")))
    except:
        return """""

def binary(string, base):
    try:
        return bin(int(string, base))
    except:
        return ""



"""def bina_to_deci(string):
    '''Converts input binary to decimal format'''
    try:
        return int(string, 2)
    except:
        return ""

def hex_to_deci(string):
    '''Converts input hex number to decimal format'''
    try:
        return int(string, 16)
    except:
        return ""

def octa_to_deci(string):
    '''Converts input octal number to decimal format'''
    try: 
        return int(string, 8)
    except:
        return """""

def decimal(string, base):
    try:
        return int(string, base)
    except:
        return ""


def octa(string, base):
    try: 
        return oct(int(string, base))
    except: 
        return ""

"""def bina_to_hexa(string):
    '''Converts input binary to hexadecimal format'''
    try:
        return hex(int(string, 2))
    except:
        return ""

def deci_to_hexa(string):
    try:
        return hex(int(string))
    except:
        return ""

def octa_to_hexa(string):
    try: 
        return hex(int(string, 8))
    except:
        return"""""

def hexa(string, base):
    ret = ""
    for s in string:
        try:
            ret = ' '.join([ret, hex(int(s, base))])
        except:
            return ret
    return ret


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