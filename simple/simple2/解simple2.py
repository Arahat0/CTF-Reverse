v8 = ":\"AL_RT^L*.?+6/46"
v7 = "harambe"
print(v8)
print(len(v8))
print(v7)
password = ''
for i in range(len(v8)):
    password += chr(ord(v7[i % 7]) ^ ord(v8[i]))
print(password)
