input_a = input("Input a: ")
input_b = input("Input b: ")
input_c = input("Input c: ")
print()

a = int(input_a)
b = int(input_b)
c = int(input_c)

print(input_a + "x^2 + " + input_b + "x + " + input_c)
print()

# Calculate the delta
delta = b ** 2 - 4 * a * c

print("Delta: ", delta)
print()

if delta > 0:
    print("Delta is greater than 0")
    print("There are two zeros of a function")
    x1 = (-b - delta ** 0.5) / 2 * a
    x2 = (-b + delta ** 0.5) / 2 * a
    print("x1: ", x1)
    print("x2: ", x2)

elif delta == 0:
    print("Delta is equal to 0")
    print("There is one zero of a function")
    x0 = -b / 2 * a
    print("x0: ", x0)

else:
    print("Delta is less than 0")
    print("There are no zeros of a function")
