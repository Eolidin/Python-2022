input = ['12', '-2', '0']
output = [12, -2, 0]
list(map(lambda x: int(x), input))
print(list(map(lambda x: int(x), input)) == output)

input = ['12', '-2', '0', '-4', '1']
output = ['12', '0', '1']
list(filter(lambda x: int(x) >= 0, input))
print(list(filter(lambda x: int(x) >= 0, input)) == output)

input = ['hello', 'world']
output = [5, 5]
list(map(lambda x: len(x), input))
print(list(map(lambda x: len(x), input)) == output)

input = ['hello', 'world']
output = ['olleh', 'dlrow']
list(map(lambda x: x[::-1], input))
print(list(map(lambda x: x[::-1], input)) == output)

input = range(20)
output = [0, 3, 5, 6, 9, 10, 12, 15, 18]
list(filter(lambda x: x % 3 == 0, input))
print(list(filter(lambda x: x % 3 == 0 or x % 5 == 0, input)) == output)

input = range(2, 6)
output = [(2, 4, 8), (3, 9, 27), (4, 16, 64), (5, 25, 125)]
list(map(lambda x: (x, x ** 2, x ** 3), input))
print(list(map(lambda x: (x, x ** 2, x ** 3), input)) == output)

input = zip(range(2, 5), range(3, 9, 2))
output = [6, 15, 28]
list(map(lambda x: (x[0] * x[1]), input))
print(list(map(lambda x: x[0] * x[1], input)) == output)  # kein plan was hier schief läuft

input = ['hello', 'world']
output = ['world']
def func(x):
    if x == input[-1]:
        return x
print(list(filter(func, input)) == output) # keine ahnung was da abgeht
