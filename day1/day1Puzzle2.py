leftColumn = []
rightColumn = []
result = []
counter = 0

with open("data.txt") as file:
    for line in file:
        num1, num2 = map(int,line.split())
        leftColumn.append(num1)
        rightColumn.append(num2)


for i in range(len(leftColumn)):
    for j in range(len(rightColumn)):
        if leftColumn[i] == rightColumn[j]:
            counter += 1

    result.append((leftColumn[i], counter))
    counter = 0

total = 0

for key, value in result:
    total += key * value;

print(total)