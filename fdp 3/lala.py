import math
a = float(input("Mostre o primeiro número: "))
b = float(input("Mostre o primeiro número: "))
c = float(input("Mostre o primeiro número: "))
if a>b>c:
    print("O maior número é",a, "e o menor número é", c)
if b>a>c:
    print("O maior número é",b, "e o menor número é", c)
if c>a>b:
    print("O maior número é",c, "e o menor número é", b)
if a>c>b:
    print("O maior número é",a, "e o menor número é", b)
if b>c>a:
    print("O maior número é",b, "e o menor número é", a)
if c>b>a:
    print("O maior número é",c, "e o menor número é", a)