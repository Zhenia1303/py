n = int(input("Wprowadz liczbu: "))

for i in range(1, n + 1):
    print(f"{i:3}", end="")
print()

print("-" * (n * 3))

for row in range(2, n + 1):
    print(f"{1:3}", end="|")
    for col in range(1, n + 1):
        print(f"{row * col:3}", end="")
    print()
