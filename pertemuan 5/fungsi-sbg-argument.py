def average(numbers):
    return sum(numbers) / len(numbers)

def aggregate(message, numbers, f):
    print(f"{message} is {f(numbers)}")

numbers = [24, 67, 22, 98, 3, 50]

aggregate("average", numbers, average)