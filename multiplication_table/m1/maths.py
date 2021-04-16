import random

pairs_of_numbers = []
exercise_points = ""


def draw_number(range_of_numbers=2, quantity=10):
    numbers = []
    for i in range(range_of_numbers):
        number = random.randint(0, quantity)
        numbers.append(number)
    return numbers


data = []


def checking_operations(numbers, results):
    results_list = []
    for number, result in zip(numbers, results):
        # data.append([number[0], number[1], int(result)])
        if number[0]+number[1] == int(result):
            data.append([number[0], number[1], int(result), True])
            results_list.append(True)
            # data.append(True)
        else:
            results_list.append(False)
            data.append([number[0], number[1], int(result), False])
            # data.append(False)
    return results_list


def draw_pars(counter):
    for i in range(counter):
        i = draw_number(2, 10)
        pairs_of_numbers.append(i)
    return pairs_of_numbers


def points(bool_list=[]):
    # exercise_points = ""
    all = len(bool_list)
    good = bool_list.count(True)
    exercise_points = f'{good}/{all}'
    return exercise_points


def add(*args):
    result = 0
    for number in args[0]:
        result += number
    return result














#
#
# def subtraction(*args):
#     result = args[0][0]
#     for number in args[0]:
#         result -= number
#     result += args[0][0]
#     return result


def multiplication(*args):
    result = args[0][0]
    for number in args[0]:
        result *= number
    if args[0][0] == 0:
        return result
    result /= args[0][0]
    return int(result)


def division(*args):
    result = args[0][0]
    for number in args[0]:
        result /= number
    if args[0][0] == 0:
        return result
    result *= args[0][0]
    return result



# def division(*args):
#     number_1 = args[0]
#     number_2 = args[1]
#     return number_1 / number_2


# print(f'dodawanie | 1 + 2 = {add(1, 2)}')
# print(f'odejowanie | 4 - 2 = {subtraction(4, 2)}')
# print(f'mnożenie | 4 * 2 = {multiplication(4, 2)}')
# print(f'dzielenie | 4 / 2 = {division(4, 2)}')
# print(draw_number(2, 10))
# n = draw_number(2, 10)
# print(n)
# print(f'dodawanie | {n} = {add(n)}')
# print(f'odejmowanie | {n} = {subtraction(n)}')
# print(f'mnożenie | {n} = {multiplication(n)}')
# ----- losowanie do dzielenia -----

# while True:
#     print(n)
#     for i in n:
#         if i == 0:
#             n = draw_number(2, 10)
#     break
#
#
# print(f'dzielenie | {n} = {division(n)}')



