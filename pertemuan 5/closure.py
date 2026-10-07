def outer_func(numbers):
    def inner_func():
        print("max:", max(numbers))
        print("min:", min(numbers))

    inner_func()

outer_func([24, 67, 22, 98, 3, 50])