def coinChange1(n):
    arr = []

    if n <= 2:
        return n

    for i in range(n//2):
        if 2**i > n:
            break
        arr.append(2**i)
       #arr.append(2**i)
    res = []
    tmp = []
    visted = [0] * len(arr)
    dfs(0,arr,tmp,res,n,visted)
    return len(res)

def dfs(idx,arr,tmp,res,remain,visted):
    if remain < 0:
        return
    if remain == 0:
         res.append(tmp[:])
         return
    for i in range(idx,len(arr)):

        if visted[i] == 2: #can use ==2 without idx+1
            continue
        tmp.append(arr[i])
        visted[i] += 1
        dfs(i,arr,tmp,res,remain-arr[i],visted)
        visted[i] -= 1
        tmp.pop()
        
def dfs2(idx,arr,tmp,res,remain,visted):
    if remain < 0:
        return
    if remain == 0:
         res.append(tmp[:])
         return
    for i in range(idx,len(arr)):
        if i > idx and arr[i-1] == arr[i]: #skip res ex: [2,4] [4,2]
            continue
        tmp.append(arr[i])
        dfs(i+1,arr,tmp,res,remain-arr[i],visted) # not idx + 1 每個coin只能用一次
        tmp.pop()
        
