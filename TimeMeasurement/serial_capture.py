from os import device_encoding
import serial as sr

port = sr.Serial(port="/dev/cu.usbserial-1410",baudrate=115200,bytesize=sr.EIGHTBITS)
try:
    data_file = open("/Users/georgemakris/Documents/Projects/AFARS/Deliverables/Software/Aircraft/Arduino_Software/Sensors/IMU/TimeMeasurement/milliseconds.csv","w")
    print("File Initialised")
except:
    print("Check file initialisation") #Printing error message for any error that might appear

print("Entering recording loop, until exit condition is met.") # Verifying the loop has been reached.
while(int(port.readline().decode()) <= 30000): # Count until 30 seconds in ms
    print(port.readline().decode()) # Print the output | .decode is to convert bytes into string
    data_file.write(port.readline().decode()) # Right to assigned file

print("Serial Capture stopped") # Verifying that loop has been exited

port.close() # Closing port since no longer needed
print("Serial Port has been closed") 
data_file.close # CLosing output file to flush and receive data from recording
print("Data capture file: {} has been closed. Check presence of data before continuing.".format(data_file.name))

