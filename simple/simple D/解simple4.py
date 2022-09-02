import base64

hex_str = '437261636b4d654a757374466f7246756e'
print(base64.b16decode(hex_str.upper()))
