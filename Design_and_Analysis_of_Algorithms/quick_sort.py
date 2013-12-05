def swap(a,i,j):
    k=a[i]
    a[i]=a[j]
    a[j]=k
    return(a)

def partion(a,p,r):
    i=p
    j=r+1
    x=a[p]
    while(True):
        i=i+1
        while a[i]<x and i<r:
            i=i+1
        j=j-1
        while a[j]>x:
            j=j-1
        if x>=j:
            break
        swap(a,i,j)
    a[p]=a[j]
    a[j]=x
    return(a,j)

def quick_sort(a,p,r):
    if p<r:
        a,q=partion(a,p,r)
        quick_sort(a,p,q-1)
        quick_sort(a,q+1,r)
    return(a)
#print(swap([2,15,34,2,1],1,2))
print(quick_sort([6,4,1,3],0,3))
