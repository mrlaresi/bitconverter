#!/usr/bin/env python

def binary(string, base):
    '''Converts input to binary format'''
    ret = ""
    for s in string:
        try:
            ret = ' '.join([ret, bin(int(s, base))])
        except:
            break
    return ret.strip()

def decimal(string, base):
    '''Converts input to decimal format'''
    ret = ""
    for s in string:
        try:
            ret = ' '.join([ret, str(int(s, base))])
        except:
            break
    return ret.strip()


def octa(string, base):
    '''Converts input to octal format'''
    ret = ""
    for s in string:
        try: 
            ret = ' '.join([ret, oct(int(s, base))])
        except: 
            break
    return ret.strip()

def hexa(string, base):
    '''Converts input to hex format'''
    ret = ""
    for s in string:
        try:
            ret = ' '.join([ret, hex(int(s, base))])
        except:
            break
    return ret.strip()

def string(stri, base):
    '''Converts input to string format'''
    ret = ""
    if base == 10:
        return ret
    if base == 8:
        stri = hexa(stri, 8)[2:]
    if base == 2:
        for s in stri:
            try:
                ret = ' '.join([ret, chr(int(s, 2))])
            except:
                continue
    else:
        if type(stri) == type([]):
            for s in stri:
                try:
                    ret = ' '.join([ret, _hex_char(s)])
                except:
                    ret
        else:
            ret = _hex_char(stri)                    
    return ret.strip()

def _hex_char(stri):
    if len(stri) % 2 != 0:
        stri = "0" + stri
    try:
        return bytes.fromhex(stri).decode("utf-8")
    except:
        return ""
