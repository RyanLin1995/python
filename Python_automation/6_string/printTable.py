tableData = [['apple', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

colWidth = [0] * len(tableData)
#print(str(len(colWidth)))
for i in range(len(colWidth)):
    com = 0
    for k in range(len(tableData[0])):
        if len(tableData[i][k]) > com:
            com = len(tableData[i][k])
    colWidth[i] = com

for i in range(len(tableData[0])):
    for k in range(len(colWidth)):
        print(tableData[k][i].rjust(colWidth[k]),end=' ')
    print('')