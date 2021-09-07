def func(one, three, two=2, four=4):
    n = str(one) + str(two) + str(three) + str(four)
    return n
print(func(1, three=3))
