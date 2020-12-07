#!/usr/bin/env python

def binary(string, base):
    ret = ""
    for s in string:
        try:
            ret = ' '.join([ret, bin(int(s, base))])
        except:
            break
    return ret.strip()

def decimal(string, base):
    ret = ""
    for s in string:
        try:
            ret = ' '.join([ret, int(s, base)])
        except:
            break
    return ret.strip()


def octa(string, base):
    ret = ""
    for s in string:
        try: 
            ret = ' '.join([ret, oct(int(s, base))])
        except: 
            break
    return ret.strip()

def hexa(string, base):
    ret = ""
    for s in string:
        try:
            ret = ' '.join([ret, hex(int(s, base))])
        except:
            break
    return ret.strip()

def string(stri, base):
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