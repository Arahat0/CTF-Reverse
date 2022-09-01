serial = "5B134977135E7D13"
name = ''
key = [16, 48, 32]

for i in range(0, len(serial), 2):
    name += chr(int(serial[i:i+2], 16) ^ key[i % 3])

print(name)
