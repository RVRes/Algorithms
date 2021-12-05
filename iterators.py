import random
from pprint import pprint
from string import ascii_letters
from sys import getsizeof

MIN_TEMP = -25
MAX_TEMP = -5

temp_series = [
    f'{random.random() * (MAX_TEMP - MIN_TEMP) + MIN_TEMP:.2f}' for _ in range(100)]


def avg_temp_1(t_series):
    temp_sum = 0
    for t in t_series:
        temp_sum += float(t)
    return temp_sum / len(t_series)


def avg_temp_2(t_series):
    return sum(map(float, t_series)) / len(t_series)


def generate_iplist():
    raw = ['192.168.' + f'{random.randint(1, 10)}.{random.randint(1, 254)} http:\\www.' +
           ''.join(random.choice(ascii_letters) for i in range(12)) + f'_link_{_}.ru' for _ in range(1000)]
    with open("Temp\файл.txt", "w") as f:
        f.write("\n".join(raw)+"\n")

    print(getsizeof(raw))

    data = [x.split(" ") for x in open("Temp\файл.txt")]
    # data = map(str.split(" "),  open("Temp\файл.txt"))
    pprint(data)



t_as_float = map(float, temp_series)

print(next(t_as_float))
print(next(t_as_float))
for t in t_as_float:
    print(f'\t{t}')

print(temp_series)
print(avg_temp_1(temp_series))
print(avg_temp_2(temp_series))
print(getsizeof(temp_series), getsizeof(t_as_float))

generate_iplist()
