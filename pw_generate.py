import string
import random
from random import shuffle, choice
def randomm_pass():
    a = {'!', '@', '#', '%', '^', '*'}
    d = string.ascii_letters
    e = list(d) + list(a)
    g = ""
    d1 = string.ascii_letters.lower()
    d2 = string.ascii_letters.upper()
    b = choice(list(a))
    b2 = choice(list(d1))
    b3 = choice(list(d2))
    f = choice(list(e))
    c1 = random.randint(0, 10)
    c2 = random.randint(0, 10)
    c3 = random.randint(0, 10)
    c4 = random.randint(0, 10)
    c5 = random.randint(0, 10)
    c6 = random.randint(0, 10)
    c7 = random.randint(0, 10)
    c8 = random.randint(0, 10)
    b4 = choice(list(d))
    b5 = choice(list(d))
    b6 = choice(list(d))
    b7 = choice(list(d))
    order1 = [b, b3, b4, b5, b6, b7, f, b2, str(c1), str(c2), str(c3), str(c4), str(c5), str(c6), str(c7), str(c8)]
    order3 = choice(list(order1))
    order4 = choice(list(order1))
    order5 = choice(list(order1))
    order6 = choice(list(order1))
    order7 = choice(list(order1))
    order8 = choice(list(order1))
    order9 = choice(list(order1))
    order10 = choice(list(order1))
    password = [order3, order4, order5, order6, order7, order8, order9, order10, ]

    shuffle(password)
    g += ''.join(password)
    print(g)
    return g

