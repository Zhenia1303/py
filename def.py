def kwadrat(num):
    return (num * num)

num = int(input("Liczba: "))

for i in range(1, num + 1):
    print(f"Kwadra liczby {i:1} = {kwadrat(i):1}")