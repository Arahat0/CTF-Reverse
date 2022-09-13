list1 = [0x21, 0x3A, 0x23, 0x24, 0x25, 0x26, 0x28, 0x29, 0x2B, 0x2D]
str1 = 'vrt~rzey{vvyt{v'
str1 = list(str1)
str2 = ''.join([chr(x) for x in list1])
flag = ''

for i in range(15):
    str1[i] = ord(str1[i]) ^ 0x5F
    for x in range(10):
        if str1[i] == ord(str2[x]):
            flag += chr(57-x)
print(flag)