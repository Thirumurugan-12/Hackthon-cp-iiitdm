

num = int(input())

for i in range(num):
    ars = int(input())
    ar = [int(i) for i in input().split()]
    ma = []
    ma.append(min(ar))
    ar.remove(min(ar))
    ma.append(max(ar))
    ar.remove(max(ar))
    #print(ma)
    mi = []
    tr = []
    while (len(ar)>0):
        mi.append(abs(sum(ma)-sum(ar)))
        tr.append([ar,ma])
        ma.append(min(ar))
        ar.remove(min(ar))
    #print(tr)
    #print(mi)

    s = mi.index(min(mi))
    print(tr[s][1])