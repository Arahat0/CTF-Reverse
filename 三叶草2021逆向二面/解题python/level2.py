def init(sbox,key,len):
    len=53
    t=[0]*256
    for i in range(256):
        t[i] = key[i%len]
    j = 0
    for i in range(256):
        j = (j+sbox[i]+t[i])%256
        sbox[i], sbox[j] = sbox[j], sbox[i]

def crypt(sbox,len):
    j=0
    for i in range(len):
        i=(i+1)%256
        j=(j+sbox[i])%256
        sbox[i], sbox[j] = sbox[j], sbox[i]
        t=(sbox[i]+sbox[j])%256
        key.append(sbox[t])

key0= 'ghseZLeUXlgUeOeNLXboiwCSLhEFPkdYOXQZfPHiZeXZaTTyowdgBoIXuXzagshNrVsBfYKctasbbUwbVSgqQMMgvzagnvVGVRWWbcMIUmgVIDZshaABuENnlrRuEIfakeBRGforSAZzhIEbtnJtMQPxAOOCYGEEhvOBBjJWHixENrvgJeEbEdmdBkOtIvebdqIBRtMpWATKPSeYLOCdMggYZXJaQHJzZpIptxYmAoFSvXtHFfugOnfVoOjdBcWGqHuUrNBAsybBbUPjYLfwpDpuRPWdZMeWisoDrvHmjZQY'
date0 = [0xE1, 0xC8, 0xF4, 0xF8, 0xB4, 0x37, 0x56, 0xAD, 0x6A, 0xE3, 0x59, 0x45, 0x36, 0xA5, 0xBB, 0x95, 0x98, 0x81, 0x22, 0x78, 0xCE, 0x0A, 0x58, 0x83, 0xD9, 0x2C, 0xFD, 0x34, 0x65, 0x18, 0x2D, 0x71, 0xB0, 0x04, 0x3B, 0xFA, 0x40, 0x35, 0xA4, 0xBE, 0x5B, 0x4C, 0x7C, 0x9B, 0x95, 0x2C, 0x5F, 0x16, 0x7A, 0x94, 0x25, 0x1E, 0xAF, 0x9D]
klen = len(key0)
key=list()
for i in key0:
    key.append(ord(i))
sbox = [i for i in range(256)]
dlen = len(date0)
date=list()
for i in date0:
    date.append(ord(chr(i)))
init(sbox,key,klen)
key=[]
crypt(sbox,dlen)
for i in range(len(date)):
    date[i]^=key[i]^0xC
date=''.join(map(chr,date))
print("加密后的数据：",date)