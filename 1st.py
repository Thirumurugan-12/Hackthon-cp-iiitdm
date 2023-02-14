num = int(input())

for i in range(num):
    nk = [int(i) for i in input().split()]
    n = nk[0]
    k = nk[1]
    ar = [int(i) for i in input().split()]
    flag = 0
    dq = []

    for i in range(len(ar)):
        if (i+1)==ar[i]:
            dq.append(ar[i])
    #print(dq)       
    ad = list(set(ar))
    count = []
    for i in ad:
        if i not in dq:
            count.append([i,ar.count(i)])
    #print(count)
    win = []
    if len(count)>0:
        ma = count[0][1]
        ind = 0
        flag = 0
        #win = []
        print(count)

        for i in range(len(count)-1):
            if count[i][1] <= count[i+1][1]:
                ma =  count[i+1][1]
                win.append(count[i+1][0])
                ind = i+1
        #print(win)
    print(len(win),end=" ")

    for i in win:
        print(i,end=" ")
    

