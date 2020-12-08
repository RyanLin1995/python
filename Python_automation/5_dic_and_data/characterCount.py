message = "Deby Lepage donated to the Django Software Foundation to support " \
          "Django development. Donate today! "
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)