def sum_then_print(*numbers):
    total = 0

    for n in numbers:
        total = total + n

    print(total)

sum_then_print(2, 3, 4, 5, 4)