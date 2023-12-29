class Student:
    def __init__(self, height, weight, idx):
        self.height = height
        self.weight = weight
        self.idx = idx

n = int(input())

students = []
for i in range(n):
    h,w = map(int,input().split())
    s = Student(h,w,i+1)
    students.append(s)

students = sorted(students, key = lambda x : (x.height, -x.weight))

for s in students:
    print(s.height, s.weight, s.idx)