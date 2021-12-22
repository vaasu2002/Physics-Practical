M = int(input("ENTER CONSTANT MASS/ MASS ON PLANK "))
friction_coff = float(input("ENTER friction coff "))
g = 9.8

m = int(input())
a = ((m - friction_coff*M)*g)/(M+m)
print(f"MEASURED:- {a}")

S = 100
S = S/100

t = float(input())
a = 2*S/(t*t)
print(f"MEASURED:- {a}")
