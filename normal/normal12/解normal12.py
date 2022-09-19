dest = [0x0000004A, 0x00000032, 0x00000032, 0x00000036, 0x00000031, 0x00000043, 0x00000036, 0x00000033, 0x0000002D, 0x00000033, 0x00000049, 0x00000032, 0x00000049, 0x0000002D, 0x00000045, 0x00000047, 0x00000045, 0x00000034, 0x0000002D, 0x00000049, 0x00000042, 0x00000043, 0x00000043, 0x0000002D, 0x00000049, 0x00000045, 0x00000034, 0x00000031, 0x00000041, 0x00000035, 0x00000049, 0x00000035, 0x00000046, 0x00000034, 0x00000048, 0x00000042]
dest = [ord(chr(i)) for i in dest]
flag = 'flag{'
for i in range(len(dest)):
    if dest[i] >= 48 and dest[i] <= 57:
        dest[i] = dest[i] + 48
        flag += chr(dest[i])
    elif dest[i] >= 58 and dest[i] <= 74:
        dest[i] = dest[i] - 17
        flag += chr(dest[i])
    else:
        flag += chr(dest[i])
flag += '}'
print(flag)
