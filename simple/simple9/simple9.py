# Embedded file name: secend.py
print "Welcome to Processor's Python Classroom Part 2!\n"
print "Now let's start the origin of Python!\n"
print 'Plz Input Your Flag:\n'
enc = raw_input()#在py3中和input一样
len = len(enc)
enc1 = []
enc2 = ''
aaa = 'ioOavquaDb}x2ha4[~ifqZaujQ#'#27
for i in range(len):
    if i % 2 == 0:
        enc1.append(chr(ord(enc[i]) + 1))#i=偶数
    else:
        enc1.append(chr(ord(enc[i]) + 2))#i=奇数

s1 = []
for x in range(3):
    for i in range(len):
        if (i + x) % 3 == 0:
            s1.append(enc1[i])

enc2 = enc2.join(s1)
if enc2 in aaa:
    print "You 're Right!"
else:
    print "You're Wrong!"
    exit(0)