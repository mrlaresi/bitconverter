#!/usr/bin/env python

import re

def binary(stri, base):
    '''Converts input to binary format'''
    if base == 0:
        stri = _to_hex(stri)
        base = 16
    ret = []

    for item in stri:
        results = []
        if is_whitespace(item):
            item = item.split()
        else:
            item = [item]
        for s in item:
            try:
                results.append(f"{int(s, base):08b}")
            except:
                break
        ret.append(results)

    i = 0
    while i < len(ret):
        ret[i] = ' '.join(ret[i]).strip()
        i += 1
      
    return '\n'.join(ret).strip()

def decimal(stri, base):
    '''Converts input to decimal format'''
    if base == 0:
        stri = _to_hex(stri)
        base = 16
    ret = []

    for item in stri:
        results = []
        if is_whitespace(item):
            item = item.split()
        else:
            item = [item]
        for s in item:
            try:
                results.append(str(int(s, base)))
            except:
                break
        ret.append(results)

    i = 0
    while i < len(ret):
        ret[i] = ' '.join(ret[i]).strip()
        i += 1
      
    return '\n'.join(ret).strip()


def octa(stri, base):
    '''Converts input to octal format'''
    if base == 0:
        stri = _to_hex(stri)
        base = 16
    ret = []

    for item in stri:
        results = []
        if is_whitespace(item):
            item = item.split()
        else:
            item = [item]
        for s in item:
            try: 
                results.append(f"{int(s, base):03o}")
            except: 
                break
        ret.append(results)
            
    i = 0
    while i < len(ret):
        ret[i] = ' '.join(ret[i]).strip()
        i += 1
      
    return '\n'.join(ret).strip()

def hexa(stri, base):
    '''Converts input to hex format'''
    if base == 0:
        return ' '.join(_to_hex(stri)).strip()
    ret = []

    for item in stri:
        results = []
        if is_whitespace(item):
            item = item.split()
        else:
            item = [item]
        for s in item:
            try:
                results.append(f"{int(s, base):02x}")
            except:
                break
        ret.append(results)
    
    i = 0
    while i < len(ret):
        ret[i] = ' '.join(ret[i]).strip()
        i += 1
      
    return '\n'.join(ret).strip()

def string(stri, base):
    '''Converts input to string format'''
    stri = hexa(stri, base)
    stri = stri.replace(' ', '20')
    stri = stri.replace('\n', '0a')
    return _to_str(stri)

def _to_str(stri):
    '''Turns hex string to utf-8'''
    try:
        return bytes.fromhex(''.join(stri)).decode("utf-8")
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

def is_whitespace(stri):
    '''Check if string contains whitespace characters'''
    return any(c.isspace() for c in stri)


def mask(stri):
    '''Converts subnet mask in "/x" format to string of bits'''
    stri = ' '.join(stri)
    if is_ip(stri) and is_mask(stri):
        return stri
    if not '/' in stri:
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
    if is_mask(ret):
        return bits_to_decimal(ret)
    return ""

def ip_to_bit(stri):
    '''Converts ip address from decimal format to string of bits'''
    ret = ""
    split = stri.split('.')
    for s in split:
        ret += str(binary(s, 10))
    return ret

def ip(stri):
    stri = ''.join(stri)
    if is_ip(stri):
        return stri
    return ""
    '''stri = stri.split("/")
    
    if len(stri) != 2:
        return ""
    if which:
        return _mask(stri[1])
    else:
        return _mask(stri[0])'''

def subnet(ip, mask):
    '''Calculate subnet address from ip address and subnet mask'''
    if not is_ip(ip):
        return ""
    if not is_ip(mask):
        return ""
        
    ip = ip.split('.')
    mask = mask.split('.')
    ret = []
    for i in range(0, 4):
        # AND operation of ip address and subnet mask
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

def is_ip(address):
    '''Check if ip address is valid address'''
    return re.match("^((25[0-5]|(2[0-4]|1[0-9]|[1-9]|)[0-9])(\.(?!$)|$)){4}$", address)

def is_mask(bitstring):
    if not is_binary(bitstring):
        bitstring = binary(bitstring.split('.'), 10)
        bitstring = ''.join(bitstring.split())
    if len(bitstring) != 32:
        return False
    i = 0
    first_zero = False
    for char in bitstring:
        if i < 8 and char == "0":
            return False
        elif i > 7 and char == "0":
            first_zero = True
        if first_zero and char == "1":
            return False
        i+=1
    return True

def is_binary(stri):
    return re.match("[01]", stri)
