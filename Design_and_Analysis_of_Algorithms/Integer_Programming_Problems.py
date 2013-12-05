def Integer_Programming_roblems(n,m):
    if n<1 or m<1:
        return(0)
    if n==1 or m==1:
        return(1)
    if n<m:
        return(Integer_Programming_roblems(n,n))
    if n==m:
        return(Integer_Programming_roblems(n,m-1)+1)
    return(Integer_Programming_roblems(n,m-1)+Integer_Programming_roblems(n-m,m))


print(Integer_Programming_roblems(6,6))
