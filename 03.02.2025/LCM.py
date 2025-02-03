import math
a, b = map(int, input("Enter two numbers: ").split())
print("LCM:", abs(a * b) // math.gcd(a, b))
