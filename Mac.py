z = 1

# a % 3 == 0


while z <= 100:
    if z % 3 == 0 and z % 5 == 0:
        print ("G")
    elif z % 3 == 0:
        print("a")
    elif z % 5 == 0:
        print("b")
    else:
        print(z)
    z = z + 1

# 1
# 2
# a
# 4
# 5
# a
# 7


