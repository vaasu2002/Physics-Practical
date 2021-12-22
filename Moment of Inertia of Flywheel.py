g = 9.8

N = float(input("Enter of revolution: "))
t = float(input("Time for N revolution(in sec): "))

angular_velocity = (4*3.14159*N)/t
angular_velocity 

n = float(input("Number of cord winding: "))
h = float(input("Height:(cm) "))
r = float(input("radius of axle:(cm) "))
m = float(input("Mass suspended:(gram) "))

i = (N*m*0.001)/(N+n)
x = ((2*h*0.01*g)/angular_velocity**2)  -  r*r*0.01*0.01
i = i*x
print(i)
