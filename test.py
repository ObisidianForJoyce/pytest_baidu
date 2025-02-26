import string
import random
import re

from numpy import array


def random_str(length=5):
    letters = string.ascii_lowercase
    print(letters)
    return ''.join(random.choice(letters) for i in range(length))

def random_email():
    print(f"{random_str()}")
    print("{}".format(random_str()))
    return f"{random_str()}@kingland.com"

def test_len():
    str1 = [11,'25',55]
    str = array(str1)
    print('the lenght is:', len(str), 'type is: ', type(str))


# print([x for x in list(map(lambda x: x * x, num_list)) if x > 10])

if __name__ == '__main__':
    print(random_email())
    test_len()
    num_list = [1, 2, 3, 4, 5]
    aa = list(map(lambda x: x * x, num_list))
    print(aa,"type is：",type(aa))
    bb=[]
    for x in aa:
        if x>10:
            bb.append(x)
    print(bb)
    print(random.uniform(2, 6))  # 指定随机小数
