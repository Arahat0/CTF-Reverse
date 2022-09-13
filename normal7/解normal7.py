import base64
str1 = 'αβγδεζηθικλμνξοπρσ89+/さしすせそたちτυφχψω012345てとゐなにぬねの67つっはひふへほゑま;'
str2 = 'すひ6ねτ3/7しはξ2すつιのν92φτひ/なしひξねたさ+ψιρ;;'
b64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
flag = ''
for i in str2:
    flag += b64[str1.index(i)]
flag = base64.b64decode(flag)
print(flag)
