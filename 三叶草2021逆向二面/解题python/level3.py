import base64
#第一步
a=[ '{:0>6}'.format(bin(i).replace('0b', '')) for i in range(64) ]
a=''.join(a)
c=[0]*48
for i in range(len(c)):
    c[i]=(int(a[i*8:i*8+8],2))
print(c)
d=''.join([hex(i) for i in c])
e=d.replace('0x','')
print('0'+e)
f='0'+e
print(f[30:96])

#第二步
box1=[0xE8, 0x56, 0x4C, 0x58, 0x1C, 0xB3, 0x26, 0x9B, 0xB8, 0x90, 0xDA, 0xD0, 0x05, 0x5E, 0x6B, 0x38, 0xD5, 0xF9, 0x25, 0xBD, 0x67, 0x57, 0xDF, 0xDD, 0xE4, 0xEA, 0xE5, 0x51, 0x6D, 0x22, 0x87, 0xBB, 0x6F, 0x33, 0xD2, 0xC0, 0x8C, 0x07, 0x44, 0xE9, 0x06, 0x3E, 0x69, 0x83, 0x82, 0xAF, 0x39, 0xF4, 0xA2, 0x97, 0x1E, 0x31, 0x7B, 0x3F, 0xBC, 0x3D, 0x3C, 0xD6, 0x1D, 0x93, 0x4B, 0xA3, 0xE7, 0xD3]
date=[0x67, 0x3F, 0x07, 0x58, 0x87, 0x3F, 0x07, 0xB8, 0xDF, 0xB3, 0xEA, 0x56, 0xE4, 0xBC, 0x3E, 0x69, 0x6D, 0x1C, 0x22, 0x31, 0xD5, 0x44, 0x97, 0x44, 0x57, 0xB3, 0x3E, 0x3D, 0x67, 0xDF, 0xAF, 0x26, 0x25, 0xBC, 0xA3, 0xDD, 0xF9, 0x07, 0x22, 0x39, 0x6D, 0x44, 0xD6, 0xA3]
en1=[0]*44
b64='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
b64list=list(b64)
for i in range(len(date)):
    for j in range(len(box1)):
        if date[i]==box1[j]:
            en1[i]=b64list[j]
b64cipher=''.join(en1)
print(len(box1))
print(b64cipher)
flag=base64.b64decode(b64cipher)
print(flag)