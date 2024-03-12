# bn = bin(10111)[2:]
# os = oct(123514265)[2:]
# szes = hex(1599)[2:]


# bn = int("01010111", 2)
# os = int('1712641',8)
# szes = int("ABABCD",16)

# print("2 :", bn)
# print("8 :", os)
# print("16 :", szes)


lista= [
    [1,2,3],
    ['jeden','dwa','trzy'],
    ['x','y','z']
]
x = list(zip(*lista))
print(x)