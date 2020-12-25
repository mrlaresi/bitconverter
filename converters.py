#!/usr/bin/env python

def binary(stri, base):
    '''Converts input to binary format'''
    if base == 0:
        stri = _to_hex(stri)
        base = 16
    ret = ""
    for s in stri:
        try:
            ret = ' '.join([ret, f"{int(s, base):08b}"])
        except:
            break
    return ret.strip()

def decimal(stri, base):
    '''Converts input to decimal format'''
    if base == 0:
        stri = _to_hex(stri)
        base = 16
    ret = ""
    for s in stri:
        try:
            ret = ' '.join([ret, str(int(s, base))])
        except:
            break
    return ret.strip()


def octa(stri, base):
    '''Converts input to octal format'''
    if base == 0:
        stri = _to_hex(stri)
        base = 16
    ret = ""
    for s in stri:
        try: 
            ret = ' '.join([ret, f"{int(s, base):03o}"])
        except: 
            break
    return ret.strip()

def hexa(stri, base):
    '''Converts input to hex format'''
    if base == 0:
        return ' '.join(_to_hex(stri)).strip()
    ret = ""
    for s in stri:
        try:
            ret = ' '.join([ret, f"{int(s, base):02x}"])
        except:
            break
    return ret.strip()

def string(stri, base):
    '''Converts input to string format'''
    return _to_str(hexa(stri, base)).strip()

def _to_str(stri):
    '''Turns hex string to utf-8'''
    try:
        return bytes.fromhex(stri).decode("utf-8")
    except:
        return ""

def _to_hex(stri):
    try:
        stri = str.encode(''.join(stri), "utf-8").hex()
        ret = []
        for i in range(0, len(stri), 2):
            ret.append(stri[i:i+2])
            i += 2
        return ret
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
    return bits_to_decimal(_ip(stri, True))

def ip(stri):
    return _ip(stri)

def subnet(ip, mask):
    '''Calculate subnet address from ip address and subnet mask'''
    ip = ip.split(".")
    mask = mask.split(".")
    ret = []
    for i in range(0, 4):
        ret.append(str(int(ip[i]) & int(mask[i])))
    return '.'.join(ret)

def broadcast(subnet, mask):
    '''Calculate broadcast address from subnet address and subnet mask'''
    subnet = subnet.split(".")
    mask = mask.split(".")
    ret = []
    for i in range(0, 4):
        ret.append(str(int(subnet[i]) | ~ int(mask[i]) & 0xFF))
    return '.'.join(ret)

def first_ip(subnet):
    subnet = subnet.split(".")
    subnet[3] = str(int(subnet[3]) + 1)
    return '.'.join(subnet)

def last_ip(subnet, mask):
    ret = broadcast(subnet, mask).split(".")
    ret[3] = str(int(ret[3]) - 1)
    return '.'.join(ret)


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
    '''Transforms 32 bit long string of bits to 8 bit long decimal numbers,
    separated by "." character'''
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
print(broadcast("192.168.1.0", "255.255.255.0"))
print(last_ip(subnet("192.168.1.144", "255.0.0.0"), "255.192.0.0"))