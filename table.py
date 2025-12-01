n = int(input("Wprowadz liczbu: "))

print(' ' * 5, end='')
for i in range(1, n + 1):
    print(f"{i:4}", end="")
print()

print("-" * (n * 4 + 6))

for row in range(2, n + 1):
    print(f"{row:4}", end="|")
    for col in range(1, n + 1):
        print(f"{row * col:4}", end="")
    print()