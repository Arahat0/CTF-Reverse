def rule(x):
    if x<=63:
        list.append(x)
        print(list  )
        rule(2*x+1)
        return(rule(2*(x+1)))

a=0
counter=0
list=[]
rule(a)