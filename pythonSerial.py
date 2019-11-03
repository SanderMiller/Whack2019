import serial
import os
import signal

arduinoComPort = "/dev/ttyACM0" # Set the com port
baudRate = 115200 # the baud rate to 250000
serialPort = serial.Serial(arduinoComPort, baudRate, timeout=1) # Set the serial port for reading

# Open a new file to store the data to
datafile = open('data.txt','a+')

# Define a keyboard interrupt function to stop the loop when done
def keyboardInterruptHandler(signal, frame):
    print("KeyboardInterrupt".format(signal))
    exit(0)

signal.signal(signal.SIGINT, keyboardInterruptHandler)

while True:
	# Read in the serial data
    lineOfData = serialPort.readline().decode()
    # Write the line of data that was read over serial
    datafile.write(lineOfData)
	# Print the line in terminal to ensure it is working
    print(str(lineOfData))
	
# Close the data file 
datafile.close()
