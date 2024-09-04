import math
p=3
q=7
n=p*q
print("n=",n)
phi=(p-1)*(q-1)
e=2
while(e<phi):
    if(math.gcd(e,phi)==1):
        break
    else:
        e+=1
print("e=",e)
k=2
d=((k*phi)+1)/e
print("d=",d)
print("public key",e,n)
print("privete key",d,n)
msg=11
print("original message is ",msg)
c=pow(msg,n)
c=math.fmod(c,n)
print("encrypted message is ",c)
m=pow(c,d)
m=math.fmod(m,n)
print("decrypted message is ",m)


