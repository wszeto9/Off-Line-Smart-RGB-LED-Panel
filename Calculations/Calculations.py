Vleds = 22
Vin = 169
Iled = 0.7

duty = Vleds/Vin

tblank = 440 * 10**-9

Rosc = 75 * 10**3

tosc = (Rosc/10**3 + 22)/25 * 10**-6

fosc = 1/tosc

L = (Vin-Vleds)*duty/(0.3 * Iled * fosc)

Cin = Iled * Vleds * 0.06 / (Vin**2)

Irr = 10 * 10**-6
trr = 35 * 10**-9
Vr = Vin 

Prr_led_driver_diode = 1/2 * Irr * trr * Vr * fosc

Rsense = 0.25/(Iled + (0.5 * (Iled * 0.3)))

print("\n\n\n\n\n\n\n\n\n\n\n")
print("duty cycle: " , round(duty,3)) 
print("Tsw (us): ", round(tosc * 10**6,1))
print("Fsw(kHz): " , round(fosc/10**3)) 
print("L(uH): ", round(L * 10**6), "IRMS(A): ", Iled, "Isat(A): ", round(Iled * 1.3,2))
print("Cin(uF): ", round(Cin * 10**6))
print("Rsense (Ohms): ", Rsense)
print("Diode switching losses(W): ", Prr_led_driver_diode)


