#coding=utf-8
def is_ordered(array):
    lengh=len(array)
    if lengh<=1:
        return(1)
    if array[0]>=array[1]:
        for i in range(lengh-1):
            if array[i]>=array[i+1]:
                flag=1
            else:
                flag=0
                break
    else:
        for i in range(lengh-1):
            if array[i]<=array[i+1]:
                flag=1
            else:
                flag=0
                break
    return(flag)

goto=1
while goto==1:
    print('')
    X=input("请输入一个数组：")
    X=list(X)
    Y=X
    t=is_ordered(Y)
    if t==0:
        print(str(X)+"是无序的。")
    elif t==1:
        print(str(X)+"是有序的。")
    goto==0
    print('')
    g=input("输入0退出，输入1继续...: ")
    g=int(g)
    if g==0:
        goto=0
    else:
        goto=1
