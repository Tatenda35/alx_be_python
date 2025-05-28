number = int(input("Enter a number to see its multiplication table: "))

for _ in range(0,11,1):
    print(f"{number} * {_} = {number * _}")