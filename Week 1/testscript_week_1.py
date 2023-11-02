import pyvisa
import time


rm = pyvisa.ResourceManager("@py")
ports = rm.list_resources()

device = rm.open_resource(
    "ASRL5::INSTR", read_termination="\r\n", write_termination="\n"
)

#Debug print
#print(device.query("*IDN?"))

out_val = 100
burn = False
data = list()

for value in range(100,1200,1):
    device.query(f"OUT:CH0 {value}")
    measurement = device.query("MEAS:CH2?")
    data.append((value,measurement))

print("Volt(mV)\t|\tMeasurement")
print(37*"-")
for val in data:
    print(f"{val[0]}\t\t|\t\t{val[1]}")