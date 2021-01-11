nums = list()

a = 0
b = 1
i = 0

while i < 10:
    nums.append(a)
    i += 1
    a, b = b, a + b

for num in nums:
    print(num)