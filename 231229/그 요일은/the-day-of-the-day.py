days = [31,29,31,30,31,30,31,31,30,31,30,31]

def countFromNew(m,d):
    counts = 0
    for i in range(m-1):
        counts += days[i]
    counts += d
    return counts

m1,d1,m2,d2 = map(int,input().split())
A = input()

day1 = countFromNew(m1,d1)
day2 = countFromNew(m2,d2)

countDays = day2 - day1

if (countDays < 7):
    print(1)
elif (countDays %  7 == 0 ):
    print(countDays // 7 + 1)
else:
    print(countDays // 7)