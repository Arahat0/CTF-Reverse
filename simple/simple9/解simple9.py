aaa = 'ioOavquaDb}x2ha4[~ifqZaujQ#'#len(aaa) = 27
enc1 = list(aaa)
enc = []
a1 = 0
a2 = 18
a3 = 9
x = 0
for i in range(9):
    enc1[x] = aaa[a1+i]
    x += 1
    enc1[x] = aaa[a2+i]
    x += 1
    enc1[x] = aaa[a3+i]
    x += 1
print(enc1)

for y in range(27):
    if y % 2 == 0:
        enc.append(chr(ord(enc1[y]) - 1))
    else:
        enc.append(chr(ord(enc1[y]) - 2))
print(''.join(enc))