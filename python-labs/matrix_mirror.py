from curses.ascii import isdigit

n = 0
while True:
    usr_input = input("Enter the size of square matrix (number must be positive): ")
    if usr_input.isdigit():
        n = int(usr_input)
    else:
        print("You need to enter positive <int> value!")
        continue
    if n > 2:
        break
    else:
        print("Number need to be greater or equals 2!")


matrix = []
for i in range(n):
    row = []
    for k in range(n):
        if k == i:
            row.append(1)
        else:
            row.append(0)
    matrix.append(row)

for i in matrix:
    print(i)

print()
print("Mirror image of identity matrix:")
for i in reversed(matrix):
    print(i)
