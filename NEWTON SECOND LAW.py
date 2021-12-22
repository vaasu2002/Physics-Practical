M = int(input("ENTER CONSTANT MASS/ MASS ON PLANK "))
friction_coff = float(input("ENTER friction coff "))
g = 9.8

m = int(input())
a = ((m - friction_coff*M)*g)/(M+m)
print(f"MEASURED:- {a}")
