N = int(input())
users = []
for _ in range(N):
    age, name = input().split()
    users.append((int(age), name))

users = sorted(users, key=lambda x: x[0])
for age, name in users:
    print(age, name)