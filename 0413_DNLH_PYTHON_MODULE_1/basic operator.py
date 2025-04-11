# Taking input
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

print("\n--- Arithmetic Operators ---")
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a // b =", a // b)
print("a % b =", a % b)
print("a ** b =", a ** b)

print("\n--- Assignment Operators ---")
x = a     # We use x for testing assignments
print("x = a →", x)
x += b
print("x += b →", x)
x -= b
print("x -= b →", x)
x *= b
print("x *= b →", x)
x /= b
print("x /= b →", x)
x %= b
print("x %= b →", x)
x //= b
print("x //= b →", x)
x **= b
print("x **= b →", x)

print("\n--- Comparison Operators ---")
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

print("\n--- Logical Operators ---")
x = True
y = False
print("x and y:", x and y)
print("x or y:", x or y)
print("not x:", not x)

print("\n--- Bitwise Operators ---")
print("a & b =", a & b)
print("a | b =", a | b)
print("a ^ b =", a ^ b)
print("~a =", ~a)
print("a << 1 =", a << 1)
print("a >> 1 =", a >> 1)

print("\n--- Identity Operators ---")
print("a is b:", a is b)
print("a is not b:", a is not b)
