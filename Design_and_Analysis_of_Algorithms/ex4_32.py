with open('input.txt') as f:
    data=f.readlines()
n=int(data[0])
##if n==0:
##    break
name={}
for i in range(n):
    name[i]=data[i+1]
r = [([0] * n) for i in range(n)]
edges=int(data[n+1])
for i in range(edges):
    Rates=data[n+i+2]
    Rates=Rates.split(' ')
    a=Rates[0]
    b=Rates[2]
    x=Rates[1]
    for j in range(n):
        if name[j]==str(a+'\n'):
            break
    for k in range(n):
        if name[k]==b:
            break
    r[j][k]=x
for i in range(n):
    r[i][i]=max(1.0,r[i][i])
for k in range(n):
    for i in range(n):
        for j in range(n):
            r[i][j]=max(float(r[i][j]),float(r[i][k])*float(r[k][j]))
for i in range(n):
    if r[i][i]>1.0:
        break
if i<n:
    print('case '+str(i)+' yes')
else:
    print("case "+str(i)+' no')
print(r)
