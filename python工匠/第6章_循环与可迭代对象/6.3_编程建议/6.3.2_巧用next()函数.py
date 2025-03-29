numbers = [3, 6, 8, 2, 21, 30, 42]
print(next(iter(i for i in numbers if i % 7 == 0)))

user_count = {
    "alice": 4,
    "bob": 2,
    "charlie": 2,
    "dave": 3,
}

print(next(iter(sorted(user_count.items(), key=lambda pair: pair[1]))))
