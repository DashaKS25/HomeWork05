#Написати функцію, яка буде підносити число у квадрат. Написати другу, яка буде перевіряти, чи є число простим. Потрібно видрукувати в головній програмі квадрати усіх простих чисел зі списку від 0 до 50 за допомогою map


def simple(number):
    for i in range(2, int(number ** 0.5) + 1):
        if not number % i:
            return False
    return True


print(list(map(lambda num: num ** 2, filter(simple, range(1, 51)))))
