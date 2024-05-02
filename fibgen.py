def fibgen(num):
    a,b=0,1
    while(num>0):
        yield a
        a,b=b,a+b
        num-=1
for n in fibgen(20):
    print(n)        

