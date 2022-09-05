def rule(x):
    if x<=63:
        list.append(x)
        rule(2*x+1)
        rule(2*(x+1))
a=0
counter=0
list=[]
rule(a)
print(list)
print(len(list))
str = 'bcec8d7dcda25d91ed3e0b720cbb6cf202b09fedbc3e017774273ef5d5581794'
flag=[0 for i in range(64)]
for i in range(len(list)):
    flag[list[i]]=str[i]
print(''.join(flag))