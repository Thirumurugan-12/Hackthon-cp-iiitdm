num = [int(i) for i in input().split()]
num = sorted(num)
s = []
for i in range(len(num)):
    t = []
    t.append(num[i])
    for j in range(len(num)):
            if (num[i]!=num[j]):
                #t = [num[i]]
                t.append(num[j])
    s.append(t)
print(s)


s1 = []
for i in s[::-1]:
    s1.append(i[::-1])
print(s1)
