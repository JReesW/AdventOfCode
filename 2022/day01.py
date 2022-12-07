with open("addenda/input01.txt", 'r') as file:
    lines = file.readlines()

elf = 1
total = []
current = []

for line in lines:
    if line.strip().isnumeric():
        current.append(int(line))
    else:
        total.append(current)
        current = []


print(sorted([sum(t) for t in total], reverse=True))
