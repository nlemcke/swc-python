x = 2
y = 0
coef = [2, 2, 2]
for idx, val in enumerate(coef):
    y = y + val * x ** idx
print(y)
