# tutorial from https://www.youtube.com/watch?v=Zee665ssm8Y&t=12s

# list can behave like a stack
def stack_and_queue():
    stack = list()
    stack.append(1)

    stack.append(2)

    pop_element = stack.pop()

    print(stack, pop_element)
    # list can behave like a queue
    queue = list()
    queue.append(1)

    queue.append(2)
    pop_element = queue.pop(0)

    print(queue, pop_element)


# iterable sets
def set_stuff():
    set1 = set([1, 2, 3, 4, 5, 6, 7])
    set2 = set([0, 2, 4, 5, 6, 8])

    intersection = set1 & set2
    print(intersection)


# list comprehension
def list_comprehension():
    lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    even_lst = [x for x in lst if x % 2 == 0]
    print(even_lst)

    square_lst = [x ** 2 for x in lst]
    print(square_lst)




if __name__ == '__main__':
    list_comprehension()
