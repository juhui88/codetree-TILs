class Data:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

n = int(input())
datas = []
for i in range(n):
    date, day, weather = input().split()
    if weather == "Rain":
        d = Data(date, day, weather)
        datas.append(d)

rainyDayIdx = 0
for i in range(len(datas)):
    if datas[rainyDayIdx].date > datas[i].date:
        rainyDayIdx = i

print(datas[rainyDayIdx].date, datas[rainyDayIdx].day, datas[rainyDayIdx].weather)