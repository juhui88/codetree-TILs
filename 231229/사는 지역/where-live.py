class Person:
    def __init__(self,name, address, city):
        self.name = name
        self.address = address
        self.city = city

n = int(input())

people = []
for i in range(n):
    name, address, city = input().split()
    p = Person(name,address,city)
    people.append(p)

idx = 0
for i, person in enumerate(people):
    if person.name > people[idx].name:
        idx = i

print("name",people[idx].name)
print("addr",people[idx].address)
print("city",people[idx].city)