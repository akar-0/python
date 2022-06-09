from random import randrange
def is_prime(p):
    if p<2: return False
    if p!=2 and p%2==0: return False
    s=p-1
    while s%2==0: s>>=1
    for _ in range(10):
        a=randrange(p-1)+1
        t=s
        r=pow(a,t,p)
        while t!=p-1 and r!=1 and r!=p-1:
            r=(r*r)%p
            t<<=1
        if r!=p-1 and t%2==0: return False
    else: return True
