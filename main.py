def sum_int_number(number):
    num = 1
    sum_result = 0
    while num < number + 1:
        sum_result = sum_result + num
        num = num + 1
    return sum_result


if __name__ == '__main__':
    print(sum_int_number(10))


