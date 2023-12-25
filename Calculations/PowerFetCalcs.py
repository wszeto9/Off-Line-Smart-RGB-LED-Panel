#FET Device specs
GateCharge = 8 * 10**-9
Rdson = 3
Tja = 55

#switching characteristics
duty = 0.2
fsw = 265000
Igate = 1
Vds = 169
Id = 0.7
Ta = 25

ConductionLoss = duty * Id **2 * Rdson

SwitchingLoss = fsw * 2 * Id * Vds * GateCharge / Igate

print(ConductionLoss)
print(SwitchingLoss)


