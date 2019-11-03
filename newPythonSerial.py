import serial
import os
import webbrowser
import csv
import time

path = 'C:\\Users\\tjagielski\\Downloads\\database.csv'
try:
    os.remove(path)
except FileNotFoundError:
    pass
url = 'https://storage.cloud.google.com/medical_records_whack2019/database.csv'
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
webbrowser.get(chrome_path).open(url)

while True:
    try:
        open(path, mode='r')
        break
    except FileNotFoundError:
        time.sleep(2)

with open(path, mode='r') as infile:
    reader = csv.reader(infile)
    with open('database_new.csv', mode='w') as outfile:
        writer = csv.writer(outfile)
        database = {rows[0]:rows[1] for rows in reader}

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

