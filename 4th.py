num = int(input())

for i in range(num):
    nk = [int(i) for i in input().split()]
    n = nk[0]
    k = nk[1]
    ar = [int(i) for i in input().split()]
    le = len(ar)

    for i in range(k):
        ar.remove(min(ar))
        ar.remove(max(ar))
    #print()
    print(sum(ar)/len(ar))