c=299
cutoff_wavelength = int(input("Enter the wavelength(in nm):  "))
Vo = c/cutoff_wavelength
print(f"CUTOFF FREQUENCY: {Vo} x 10^15 Hz")
h = 6.62
work_function = h*Vo/1.6
print(f"WORK FUNCTION: {h*Vo/1.6} eV")

wavelength = int(input("Enter the wavelength in nm "))
V = c/wavelength
print(f"FREQUENCY: {V} x 10^15")
Kmax = h*V/1.6 - work_function
print(Kmax)
