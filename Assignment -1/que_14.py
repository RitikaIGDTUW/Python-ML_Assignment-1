print("Enter multiple lines of input (press Enter on an empty line to finish):")
lines = []

while True:
    line = input()
    if line == "":
        break
    lines.append(line)

print("\nYou entered:")
for line in lines:
    print(line)