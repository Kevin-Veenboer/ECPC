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

for value in range(100,1800,25):
    device.query(f"OUT:CH0 {value}")
    measurement = device.query("MEAS:CH2?")
    data.append((value,measurement))

print("Volt(mV)\t|\tMeasurement")
for val in data:
    print(f"{data(0)}\t|\t{data(1)}")