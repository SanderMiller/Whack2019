import serial
import os
import webbrowser

database = {"0xC20x990x1C0xD6":"https://docs.google.com/document/d/1JWIO01pAdhlpUISugQuLWfZdpgDrkwkN2ll5hrF5qDg/edit?usp=sharing",
            "0xCD0xB50x100xE3":"https://docs.google.com/document/d/1_W3Q1jjn5aDbLScUpsEjmpbmuLKEAJKA8RI6aIDQfyI/edit?usp=sharing",
            "cauwqb":"https://docs.google.com/document/d/1A4Na9hsh-buNMYkypeJgEfV9cyoVbRGJ4mvidmuGVv8/edit?usp=sharing"}

arduinoComPort = "COM13" # Set the com port
baudRate = 115200 # the baud rate to 250000
serialPort = serial.Serial(arduinoComPort, baudRate, timeout=1) # Set the serial port for reading

# Open a new file to store the data to
datafile = open('data.txt','a+')

ID = ''

while len(ID) < 4:
	# Read in the serial data
    ID = serialPort.readline().decode()
    if "TIMEOUT!" in str(ID):
        ID = ''
    ID = ID.replace(" ","")
    ID = ID.strip("\r\n")
    # Write the line of data that was read over serial
    datafile.write(ID)
    # Print the line in terminal to ensure it is working
    print(str(ID))
	
datafile.close()

if str(ID) not in database:
    database[ID] = input("Link to person's medical files: ")
link = database[str(ID)]
webbrowser.open(link)

