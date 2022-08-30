import base64

def decode(correct):
    flag=''
    correct = base64.b64decode(correct)
    for i in correct:
        x= i-16
        x= x ^ 32
        flag+= chr(x)
    return flag

correct = 'XlNkVmtUI1MgXWBZXCFeKY+AaXNt'
flag=decode(correct)
print(flag)