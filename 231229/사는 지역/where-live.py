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
        target_idx = i

print("name",people[i].name)
print("addr",people[i].address)
print("city",people[i].city)