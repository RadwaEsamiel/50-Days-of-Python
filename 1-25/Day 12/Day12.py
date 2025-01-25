def is_prime(num):
    flag = True
    for number in range(1,100):
        if num%number == 0 and number!=num and number != 1:
            flag = False
    return flag


print(is_prime(73))

_____________________________________________________________________________-


def is_prime(num):
    flag = True
    for number in range(1,100):
        if num%number == 0 and number!=num and number != 1:
            flag = False
    return flag