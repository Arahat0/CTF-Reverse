import base64
s2 = 'OBufaa21Td86rWS8Wob8iGhZYocbr5vxZfcCoWv3'
key1 = 'nopqrstuvwxyzabcdefghijklm0123456789ABCDEFGHIJKL+/MNOPQRSTUVWXYZ'
key2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
v5 = ''
for i in s2:
    v5 += key2[key1.index(i)]
v5 = base64.b64decode(v5)
print(v5)
flag = ''
for i in range(len(v5)):
    if i & 1 == 1:
        flag += chr(v5[i] ^ 96)
    else:
        flag += chr(v5[i] ^ 145)
print(flag)