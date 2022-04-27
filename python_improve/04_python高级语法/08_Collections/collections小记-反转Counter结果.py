from collections import defaultdict, Counter

a = ['Brian Munoz', 'Chelsea Calderon', 'Leslie Edwards', 'Stacey Morris', 'Jeffrey Hebert', 'Scott Harrington', 'Lance Petty', 'Julie Davis', 'Darlene James', 'Travis Hernandez','Brian Munoz', 'Chelsea Calderon', 'Jeffrey Hebert', 'Scott Harrington', 'Lance Petty', 'Julie Davis',  'Chelsea Calderon', 'Leslie Edwards', 'Stacey Morris', 'Jeffrey Hebert', 'Scott Harrington', 'Lance Petty', 'Julie Davis', 'Darlene James', 'Travis Hernandez''Brian Munoz', 'Chelsea Calderon', 'Leslie Edwards', 'Scott Harrington', 'Lance Petty', 'Julie Davis', 'Darlene James', 'Travis Hernandez']
b = Counter(a)
c = (sorted(dict(b).items(), key=lambda x: x[1], reverse=False))
result = defaultdict(int)
for i in c:
    result[i[0]] = i[1]
print(dict(result))