number = int(input("Enter a number to see its multiplication table: "))

for _ in range(1,11):
    print(f"{number} * {_} = {number * _}")