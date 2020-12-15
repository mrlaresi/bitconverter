#!/usr/bin/env python

def binary(stri, base):
    '''Converts input to binary format'''
    ret = ""
    for s in stri:
        try:
            ret = ' '.join([ret, bin(int(s, base))])
        except:
            break
    return ret.strip()

def decimal(stri, base):
    '''Converts input to decimal format'''
    ret = ""
    for s in stri:
        try:
            ret = ' '.join([ret, str(int(s, base))])
        except:
            break
    return ret.strip()


def octa(stri, base):
    '''Converts input to octal format'''
    ret = ""
    for s in stri:
        try: 
            ret = ' '.join([ret, oct(int(s, base))])
        except: 
            break
    return ret.strip()

def hexa(stri, base):
    '''Converts input to hex format'''
    ret = ""
    for s in stri:
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


def _mask(stri):
    '''Converts subnet mask in "/x" format to string of bits'''
    if len(stri) > 3:
        return ""
    ret = ""
    try:
        stri = int(stri)
    except:
        return ret
    i = 0
    while i < 32:
        if i < stri: 
            ret += "1"
        else:
            ret += "0"
        i += 1
    return ret

def ip_to_bit(stri):
    '''Converts ip address from decimal format to string of bits'''
    ret = ""
    split = stri.split('.')
    for s in split:
        ret += str(binary(s, 10))
    return ret

def mask(stri):
    return _ip(stri, True)

def ip(stri):
    return _ip(stri)

def _ip(stri, which=False):
    if type(stri) == type([]):
        stri = ''.join(stri)
    stri = stri.split("/")
    if len(stri) != 2:
        return ""
    if which:
        return _mask(stri[1])
    else:
        return _mask(stri[0])

def bits_to_decimal(stri):
    '''Transforms 32 bit long string of bits to corresponding decimal numbers'''
    if len(stri) != 32:
        return ""
    jump = 0
    ret = ""
    # Give input to converter as 8 bit long pieces
    while jump < 32:
        ret += decimal([stri[jump:(jump+8)]], 2) + "."
        jump += 8
    return ret[:-1]

'''print(bits_to_decimal(ip("bepsis/31")))
ip("bepsis")
ip("/ree")
print(bits_to_decimal(ip("/1")))'''