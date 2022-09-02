import string
import re
enc2 = ''
letters = list(string.ascii_letters) + list(string.digits) + ['+', '/']#abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/
dec = 'FcjTCgD1EffEm2rPC3bTyL5Wu2bKBI9KAZrwFgrUygHN'
dec = list(dec)
a = []
x = 0
while x < len(letters):
    a = letters[x]
    for i in range(len(dec)):
        if dec[i] == a:
            dec[i] = x
    x += 1
temp_str_list = dec
for i in range(len(dec)):
    temp_str_list[i] = bin(dec[i])
temp_str_list = ['{:0>6}'.format(str(i).replace('0b', '')) for i in temp_str_list ]
temp_str = ''.join(temp_str_list)
temp_str = re.findall(r'\w{8}', temp_str)
for i in temp_str:
    enc2 += chr(int(i, 2))
lst = list(enc2)
for i in range(len(lst)):
    if i % 2 == 0:
        lst[i] = chr(ord(lst[i]) + 2)
    lst[i] = chr(ord(lst[i]) - 1)
enc = lst[::-1]
flag = ''.join(enc)
print(flag)
