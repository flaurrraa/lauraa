grade = 80
match grade:
    case 100:
        message = "perfect"
    case 90:
        message = "awsome"
    case _:
        message = "keep learning"
print(message)